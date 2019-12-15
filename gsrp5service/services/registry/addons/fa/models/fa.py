from gsrp5service.orm import fields
from gsrp5service.orm.model import Model

class fa_accounts_type(Model):
	_name = "fa.accounts.type"
	_description = "Genaral Model Account Type"
	_columns = {
	'name': fields.varchar(label='Account Type', translate=True),
	'include_initial_balance': fields.boolean(label="Bring Accounts Balance Forward", help="Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set."),
	'type': fields.selection(label='Type',selections=[
		('other', 'Regular'),
		('receivable', 'Receivable'),
		('payable', 'Payable'),
		('liquidity', 'Liquidity'),
	], required=True,
		help="The 'Internal Type' is used for features available on "\
		"different types of accounts: liquidity type is for cash or bank accounts"\
		", payable/receivable is for vendor/customer accounts."),
	'note': fields.text(label='Note')
	}
	_default = {
		'type':'other'
		}

fa_accounts_type()

class fa_accounts_tag(Model):
	_name = 'fa.accounts.tag'
	_description = 'General Model Account Tag'
	_columns = {
	'name': fields.varchar(label='Name'),
	'applicability': fields.selection(selections=[('accounts', 'Accounts'), ('taxes', 'Taxes')], label="Applicability", required=True),
	'color': fields.integer(label='Color Index'),
	'inactive': fields.boolean(label='Inactive', help="Set active to false to hide the Account Tag without removing it.")
	}
	default = {
	'applicability':'accounts'
		}

fa_accounts_tag()

class fa_accounts(Model):
	_name = "fa.accounts"
	_description = "Genaral Model Account"
	_order = "code"
	_columns = {
	'name': fields.varchar(label='Name'),
	'currency_id': fields.many2one(obj='md.currency', label='Account Currency',
		help="Forces all moves for this account to have this account currency."),
	'code': fields.varchar(label='Code',size=64, required=True),
	'deprecated': fields.boolean(label='Deprecated'),
	'user_type_id': fields.many2one(obj='fa.accounts.type', label='Type', required=True,
		help="Account Type is used for information purpose, to generate country-specific legal reports, and set the rules to close a fiscal year and generate opening entries."),
	'internal_type': fields.selection(selections=[('user','User')], label="Internal Type", readonly=True),
	'last_time_entries_checked': fields.datetime(label='Latest Invoices & Payments Matching Date', readonly=True,
		help='Last time the invoices & payments matching was performed on this account. It is set either if there\'s not at least '\
		'an unreconciled debit and an unreconciled credit Or if you click the "Done" button.'),
	'reconcile': fields.boolean(label='Allow Reconciliation',
		help="Check this box if this account allows invoices & payments matching of journal items."),
	'tax_ids': fields.many2many(obj='fa.accounts.tax', rel='fa_account_tax_default_rel',
		id1='account_id', id2='tax_id', label='Default Taxes'),
	'note': fields.text(label='Internal Notes'),
	'company_id': fields.many2one(obj='md.company', label='Company', required=True),
	'tag_ids': fields.many2many(obj='fa.accounts.tag', rel='fa_account_accounts_tag', id1='account_id', id2='tag_id', label='Tags'),
	'group_id': fields.many2one(label='Group',obj='fa.accounts.group'),

	'opening_debit': fields.numeric(label="Opening debit", compute='_compute_opening_debit_credit', help="Opening debit value for this account."),
	'opening_credit': fields.numeric(label="Opening credit", compute='_compute_opening_credit_debit', help="Opening credit value for this account.")
	}

	_sql_constraints = [
		('code_company_uniq', 'unique (code,company_id)', 'The code of the account must be unique per company !')
	]

	_default = {
	'Company': 'My Company'
	}

	_no_copy = ['last_time_entries_checked']
	
	_indicies = {
		'code':'code',
		'deprecated':'deprecated'
	}

	def _compute_opening_debit_credit(self,cr,pool,uid,record,context={}):
		return 0.00

	def _compute_opening_credit_debit(self,cr,pool,uid,record,context={}):
		return 0.00

fa_accounts()

class fa_accounts_group(Model):
	_name = "fa.accounts.group"
	_description ="Genaral Model Accounts Group"
	_order = 'code_prefix'
	_columns = {
	'name': fields.varchar(label='name'),
	'code_prefix': fields.varchar(label='Code Prefix'),
	'parent_id': fields.many2one(label='Parent',obj='fa.accounts.group', on_delete='c'),
	'childs_id': fields.one2many(label='Childs',obj='fa.accounts.group', rel='parent_id')
	}


fa_accounts_group()

class fa_accounts_journal(Model):
	_name = "fa.accounts.journal"
	_description = "General Model Accounts Journal"
	_order = 'sequence, type, code'
	_columns = {
	'name': fields.varchar(label='Journal Name'),
	'code': fields.varchar(label='Short Code', size=5, required=True, help="The journal entries of this journal will be named using this prefix."),
	'inactive': fields.boolean(label='Inactive', help="Set active to false to hide the Journal without removing it."),
	'type': fields.selection(label='Type',selections=[
			('sale', 'Sale'),
			('purchase', 'Purchase'),
			('cash', 'Cash'),
			('bank', 'Bank'),
			('general', 'Miscellaneous'),
		], required=True,
		help="Select 'Sale' for customer invoices journals.\n"\
		"Select 'Purchase' for vendor bills journals.\n"\
		"Select 'Cash' or 'Bank' for journals that are used in customer or vendor payments.\n"\
		"Select 'General' for miscellaneous operations journals."),
	'type_control_ids': fields.many2many(obj='fa.accounts.type', rel='fa_account_journal_type_rel', id1='journal_id', id2='type_id', label='Account Types Allowed'),
	'account_control_ids': fields.many2many(obj='fa.accounts', rel='fa_accounts_type_rel', id1='journal_id', id2='account_id', label='Accounts Allowed',
		domain=[('deprecated', '=', False)]),
	'default_credit_account_id': fields.many2one(obj='fa.accounts', label='Default Credit Account',
		domain=[('deprecated', '=', False)], help="It acts as a default account for credit amount"),
	'default_debit_account_id': fields.many2one(obj='fa.accounts', label='Default Debit Account',
		domain=[('deprecated', '=', False)], help="It acts as a default account for debit amount"),
	'update_posted': fields.boolean(label='Allow Cancelling Entries',
		help="Check this box if you want to allow the cancellation the entries related to this journal or of the invoice related to this journal"),
	'group_invoice_lines': fields.boolean(label='Group Invoice Lines',
		help="If this box is checked, the system will try to group the accounting lines when generating them from invoices."),
	#'sequence_id': fields.many2one(obj='ir.sequence', Label='Entry Sequence',
		#help="This field contains the information related to the numbering of the journal entries of this journal.", required=True, copy=False),
	#'refund_sequence_id': fields.many2one(obj='ir.sequence', label='Credit Note Entry Sequence',
		#help="This field contains the information related to the numbering of the credit note entries of this journal.", copy=False),
	'sequence': fields.integer(label='Sequence',help='Used to order Journals in the dashboard view'),
	'sequence_number_next': fields.integer(label='Next Number',
		help='The next sequence number will be used for the next invoice.',
		#compute='_compute_seq_number_next',
		#inverse='_inverse_seq_number_next'
		),
	'refund_sequence_number_next': fields.integer(label='Credit Notes: Next Number',
		help='The next sequence number will be used for the next credit note.',
		#compute='_compute_refund_seq_number_next',
		#inverse='_inverse_refund_seq_number_next'
		),

	#groups_id = fields.many2many('res.groups', 'account_journal_group_rel', 'journal_id', 'group_id', string='Groups'),
	'currency_id': fields.many2one(obj='md.currency', help='The currency used to enter statement', label="Currency"),
	'company_id': fields.many2one(obj='md.company', label='Company', required=True,	help="Company related to this journal"),
	'refund_sequence': fields.boolean(label='Dedicated Credit Note Sequence', help="Check this box if you don't want to share the same sequence for invoices and credit notes made from this journal"),

	'inbound_payment_method_ids': fields.many2many(obj='fa.accounts.payment.method', rel='fa_journal_inbound_payment_method_rel', id1='journal_id', id2='inbound_payment_method',
		domain=[('payment_type', '=', 'inbound')], label='Debit Methods'),
	'outbound_payment_method_ids': fields.many2many(obj='fa.accounts.payment.method', rel='fa_account_journal_outbound_payment_method_rel', id1='journal_id', id2='outbound_payment_method',
		domain=[('payment_type', '=', 'outbound')], label='Payment Methods'),
	'at_least_one_inbound': fields.boolean(label='At least one inbound',compute='_methods_compute'),
	'at_least_one_outbound': fields.boolean(label='At least one outbound',compute='_methods_compute'),
	'profit_account_id': fields.many2one(obj='fa.accounts', label='Profit Account', domain=[('deprecated', '=', False)], help="Used to register a profit when the ending balance of a cash register differs from what the system computes"),
	'loss_account_id': fields.many2one(obj='fa.accounts', label='Loss Account', domain=[('deprecated', '=', False)], help="Used to register a loss when the ending balance of a cash register differs from what the system computes"),

	'belongs_to_company': fields.boolean(label='Belong to the user\'s current company', compute="_belong_to_company"),

	# Bank journals fields
	#'bank_account_id': fields.many2one(obj='md.partners.bank', label="Bank Account", on_delete='r', domain="[('partner_id','=', company_id)]"),
	'bank_statements_source': fields.selection(selections=[('undefined', 'Undefined Yet'),('manual', 'Record Manually')], label='Bank Feeds'),
	'bank_acc_number': fields.varchar(label='Bank ACC number'),
	'bank_id': fields.many2one(label='Bank',obj='md.banks'),
	}

	_default = {
		'sequence':10,
		'company_id':'My Company',
		'inbound_payment_method_ids':'abc',
		'bank_statements_source':'undefined'
	}

	_no_copy = ['bank_account_id']

	_sql_constraints = [
		('code_company_uniq', 'unique (code, name, company_id)', 'The code and name of the journal must be unique per company !'),
	]

fa_accounts_journal()

class fa_accounts_tax_group(Model):
	_name = 'fa.accounts.tax.group'
	_order = 'sequence asc'
	_description = 'General Model Account Tax Group'
	_columns = {
	'name': fields.varchar(label='Name', translate=True),
	'sequence': fields.integer(label='Sequence')
	}

	_default = {
		'sequence':10
	}

fa_accounts_tax_group()

class fa_accounts_tax(Model):
	_name = 'fa.accounts.tax'
	_description = 'General Model Accounts Tax'
	_order = 'sequence asc'
	_columns = {
	'name': fields.varchar(label='Tax Name', translate=True),
	'type_tax_use': fields.selection(selections=[('sale', 'Sales'), ('purchase', 'Purchases'), ('none', 'None')], label='Tax Scope', required=True,
		help="Determines where the tax is selectable. Note : 'None' means a tax can't be used by itself, however it can still be used in a group."),
	'tax_adjustment': fields.boolean(label='Tax adjustment',help='Set this field to true if this tax can be used in the tax adjustment wizard, used to manually fill some data in the tax declaration'),
	'amount_type': fields.selection(label="Tax Computation", required=True,selections=[('group', 'Group of Taxes'), ('fixed', 'Fixed'), ('percent', 'Percentage of Price'), ('division', 'Percentage of Price Tax Included')]),
	'inactive': fields.boolean(label='Inactive',help="Set active to false to hide the tax without removing it."),
	'company_id': fields.many2one(obj='md.company', label='Company', required=True),
	'children_tax_ids': fields.many2many(obj='fa.accounts.tax', rel='fa_accounts_tax_filiation_rel', id1='parent_tax', id2='child_tax', label='Children Taxes'),
	'sequence': fields.integer(required=True, help="The sequence field is used to define order in which the tax lines are applied."),
	'amount': fields.numeric(label='Amont',required=True, size=(16, 4)),
	'account_id': fields.many2one(obj='fa.accounts', domain=[('deprecated', '=', False)], label='Tax Account', on_delete='r',help="Account that will be set on invoice tax lines for invoices. Leave empty to use the expense account."),
	'refund_account_id': fields.many2one(obj='fa.accounts', domain=[('deprecated', '=', False)], label='Tax Account on Credit Notes', on_delete='r',help="Account that will be set on invoice tax lines for credit notes. Leave empty to use the expense account."),
	'description': fields.varchar(label='Label on Invoices', translate=True),
	'price_include': fields.boolean(label='Included in Price',help="Check this if the price you use on the product and invoices includes this tax."),
	'include_base_amount': fields.boolean(label='Affect Base of Subsequent Taxes', help="If set, taxes which are computed after this one will be computed based on the price tax included."),
	'analytic': fields.boolean(label="Include in Analytic Cost", help="If set, the amount computed by this tax will be assigned to the same analytic account as the invoice line (if any)"),
	'tag_ids': fields.many2many(obj='fa.accounts.tag', rel='fa_account_tax_account_tag', id1='account_tax', id2='account_tag', label='Tags'),
	'tax_group_id': fields.many2one(obj='fa.accounts.tax.group', label="Tax Group", required=True),
	# Technical field to make the 'tax_exigibility' field invisible if the same named field is set to false in 'res.company' model
	'hide_tax_exigibility': fields.boolean(label='Hide Use Cash Basis Option'),
	'tax_exigibility': fields.selection(
		selections=[('on_invoice', 'Based on Invoice'),
		 ('on_payment', 'Based on Payment'),
		], label='Tax Due', 
		help="Based on Invoice: the tax is due as soon as the invoice is validated.\n"
		"Based on Payment: the tax is due as soon as the payment of the invoice is received."),
	'cash_basis_account': fields.many2one(
		obj='fa.accounts',
		label='Tax Received Account',
		domain=[('deprecated', '=', False)],
		help='Account used as counterpart for the journal entry, for taxes eligible based on payments.')
		}

	_default = {
		'type_tax_use':'sale',
		'company_id':'Me Company',
		'amount_type':'percent',
		'sequence':1,
		'tax_group_id':'g1',
		'tax_exigibility':'on_invoice'
	}

	_sql_constraints = [
		('name_company_uniq', 'unique(name, company_id, type_tax_use)', 'Tax names must be unique !'),
	]

fa_accounts_tax()

class fa_accounts_reconcile_model(Model):
	_name = "fa.accounts.reconcile.model"
	_description = "General Model Accounts Reconcile"
	_columns = {
	'name': fields.varchar(label='Button Label'),
	'sequence': fields.integer(label='Sequence',required=True),
	'has_second_line': fields.boolean(label='Add a second line'),
	'company_id': fields.many2one(obj='md.company', label='Company', required=True),

	'account_id': fields.many2one(obj='fa.accounts', label='Account', on_delete='c', domain=[('deprecated', '=', False)]),
	'journal_id': fields.many2one(obj='fa.accounts.journal', label='Journal', on_delete='c', help="This field is ignored in a bank statement reconciliation."),
	'label': fields.varchar(label='Journal Item Label'),
	'amount_type': fields.selection(label='Amount Type',selections=[
		('fixed', 'Fixed'),
		('percentage', 'Percentage of balance')
		], required=True),
	'amount': fields.numeric(label='Amount', size=(15,0), required=True, help="Fixed amount will count as a debit if it is negative, as a credit if it is positive."),
	'tax_id': fields.many2one(obj='fa.accounts.tax', label='Tax', on_delete='r'),
	#'analytic_account_id': fields.many2one(obj='fa.accounts.analytic.account', label='Analytic Account', on_delete='n'),

	'second_account_id': fields.many2one(obj='fa.accounts', label='Second Account', on_delete='c', domain=[('deprecated', '=', False)]),
	'second_journal_id': fields.many2one(obj='fa.accounts.journal', label='Second Journal', on_delete='c', help="This field is ignored in a bank statement reconciliation."),
	'second_label': fields.varchar(label='Second Journal Item Label'),
	'second_amount_type': fields.selection(selections=[
		('fixed', 'Fixed'),
		('percentage', 'Percentage of amount'),
		], label="Second Amount type",required=True),
	'second_amount': fields.numeric(label='Second Amount', size=(15,0), required=True, help="Fixed amount will count as a debit if it is negative, as a credit if it is positive."),
	'second_tax_id': fields.many2one(obj='fa.accounts.tax', label='Second Tax', on_delete='r', domain=[('type_tax_use', '=', 'purchase')]),
	#'second_analytic_account_id': fields.many2one(obj='fa.accounts.analytic.account', label='Second Analytic Account', on_delete='n')
	}

	_default = {
		'company_id': 'My Company',
		'amount': 100,
		'second_amount_type':'percentage',
		'second_amount':100
	}

fa_accounts_reconcile_model()

class fa_account_template(Model):
	_name = "fa.account.template"
	_description = 'Genaral Model Templates for Accounts'
	_order = "code"
	_columns = {
	'name':fields.varchar(label="name",required=True),
	'currency_id':fields.many2one(obj='md.currency', label='Account Currency', help="Forces all moves for this account to have this secondary currency."),
	'code':fields.varchar(label='Code',size=64, required=True),
	'user_type_id':fields.many2one(obj='fa.accounts.type', label='Type', required=True, 
		help="These types are defined according to your country. The type contains more information "\
		"about the account and its specificities."),
	'reconcile':fields.boolean(label='Allow Invoices & payments Matching',
		help="Check this option if you want the user to reconcile entries in this account."),
	'note':fields.text(label='Note'),
	'tax_ids':fields.many2many(obj='fa.tax.template', rel='fa_account_template_tax_rel', id2='account_id', id1='tax_id', label='Default Taxes'),
	'nocreate':fields.boolean(label='Optional Create',
		help="If checked, the new chart of accounts will not contain this by default."),
	'chart_template_id':fields.many2one(obj='fa.chart.template', label='Chart Template',
		help="This optional field allow you to link an account template to a specific chart template that may differ from the one its root parent belongs to. This allow you "
			"to define chart templates that extend another and complete it with few new accounts (You don't need to define the whole structure that is common to both several times)."),
	'tag_ids':fields.many2many(obj='fa.accounts.tag', rel='fa_account_template_account_tag', label='Account tag', id1='template_id',id2='tag_id', help="Optional tags you may want to assign for custom reporting"),
	'group_id':fields.many2one(label='Group',obj='fa.accounts.group')
	}

fa_account_template()

class fa_chart_template(Model):
	_name = "fa.chart.template"
	_description = "Genaral Model Templates for Account Chart"
	_columns = {
	'name':fields.varchar(label='name',required=True),
	'company_id':fields.many2one(obj='md.company', label='Company'),
	'parent_id':fields.many2one(obj='fa.chart.template', label='Parent Chart Template'),
	'code_digits':fields.integer(label='# of Digits', required=True, help="No. of Digits to use for account code"),
	'visible':fields.boolean(label='Can be Visible?',
		help="Set this to False if you don't want this template to be used actively in the wizard that generate Chart of Accounts from "
			"templates, this is useful when you want to generate accounts of this template only when loading its child template."),
	'currency_id':fields.many2one(obj='md.currency', label='Currency', required=True),
	'use_anglo_saxon':fields.boolean(label="Use Anglo-Saxon accounting"),
	'complete_tax_set':fields.boolean(label='Complete Set of Taxes',
		help="This boolean helps you to choose if you want to propose to the user to encode the sale and purchase rates or choose from list "
			"of taxes. This last choice assumes that the set of tax defined on this template is complete"),
	'account_ids':fields.one2many(obj='fa.account.template', rel='chart_template_id', label='Associated Account Templates'),
	'tax_template_ids':fields.one2many(obj='fa.tax.template', rel='chart_template_id', label='Tax Template List',
		help='List of all the taxes that have to be installed by the wizard'),
	'bank_account_code_prefix':fields.varchar(label='Prefix of the bank accounts'),
	'cash_account_code_prefix':fields.varchar(label='Prefix of the main cash accounts'),
	'transfer_account_id':fields.many2one(obj='fa.account.template', label='Transfer Account', required=True,
		domain=[('reconcile', '=', True), ('user_type_id.id', '=', '')],
		help="Intermediary account used when moving money from a liquidity account to another"),
	'income_currency_exchange_account_id':fields.many2one(obj='fa.account.template',
		label="Gain Exchange Rate Account", domain=[('internal_type', '=', 'other'), ('deprecated', '=', False)]),
	'expense_currency_exchange_account_id':fields.many2one(obj='fa.account.template',
		label="Loss Exchange Rate Account", domain=[('internal_type', '=', 'other'), ('deprecated', '=', False)]),
	'property_account_receivable_id':fields.many2one(obj='fa.account.template', label='Receivable Account'),
	'property_account_payable_id':fields.many2one(obj='fa.account.template', label='Payable Account'),
	'property_account_expense_categ_id':fields.many2one(obj='fa.account.template', label='Category of Expense Account'),
	'property_account_income_categ_id':fields.many2one(obj='fa.account.template', label='Category of Income Account'),
	'property_account_expense_id':fields.many2one(obj='fa.account.template', label='Expense Account on Product Template'),
	'property_account_income_id':fields.many2one(obj='fa.account.template', label='Income Account on Product Template'),
	'property_stock_account_input_categ_id':fields.many2one(obj='fa.account.template', label="Input Account for Stock Valuation"),
	'property_stock_account_output_categ_id':fields.many2one(obj='fa.account.template', label="Output Account for Stock Valuation"),
	'property_stock_valuation_account_id':fields.many2one(obj='fa.account.template', label="Account Template for Stock Valuation")
	}
	
	_default = {
	'code_digits':6,
	'visible':True,
	'complete_tax_set':True
	}

fa_chart_template()

class fa_tax_template(Model):
	_name = 'fa.tax.template'
	_description = 'General Model Templates for Taxes'
	_columns = {
	'chart_template_id':fields.many2one(obj='fa.chart.template', label='Chart Template', required=True),
	'name':fields.varchar(label='Tax Name', required=True),
	'type_tax_use':fields.selection(selections=[('sale', 'Sales'), ('purchase', 'Purchases'), ('none', 'None')], label='Tax Scope', required=True,
		help="Determines where the tax is selectable. Note : 'None' means a tax can't be used by itself, however it can still be used in a group."),
	'tax_adjustment':fields.boolean(label="Tax Adjustment"),
	'amount_type':fields.selection(label="Tax Computation", required=True,
		selections=[('group', 'Group of Taxes'), ('fixed', 'Fixed'), ('percent', 'Percentage of Price'), ('division', 'Percentage of Price Tax Included')]),
	'active':fields.boolean(label='Active',help="Set active to false to hide the tax without removing it."),
	'company_id':fields.many2one(obj='md.company', label='Company', required=True),
	'children_tax_ids':fields.many2many(obj='fa.tax.template', rel='fa_tax_template_filiation_rel', id1='parent_tax', id2='child_tax', label='Children Taxes'),
	'sequence':fields.integer(label='Sequence',required=True,
		help="The sequence field is used to define order in which the tax lines are applied."),
	'amount':fields.float(label='Amount',required=True),
	'account_id':fields.many2one(obj='fa.account.template', label='Tax Account', on_delete='r',
		help="Account that will be set on invoice tax lines for invoices. Leave empty to use the expense account."),
	'refund_account_id':fields.many2one(obj='fa.account.template', label='Tax Account on Refunds', on_delete='r',
		help="Account that will be set on invoice tax lines for refunds. Leave empty to use the expense account."),
	'description':fields.varchar(label='Display on Invoices'),
	'price_include':fields.boolean(label='Included in Price',
		help="Check this if the price you use on the product and invoices includes this tax."),
	'include_base_amount':fields.boolean(label='Affect Subsequent Taxes',
		help="If set, taxes which are computed after this one will be computed based on the price tax included."),
	'analytic':fields.boolean(label="Analytic Cost", help="If set, the amount computed by this tax will be assigned to the same analytic account as the invoice line (if any)"),
	'tag_ids':fields.many2many(obj='fa.accounts.tag', label='Account tag', rel='fa_tax_template_tag_rel', id1='template_id',id2='tag_id',help="Optional tags you may want to assign for custom reporting"),
	'tax_group_id':fields.many2one(obj='fa.accounts.tax.group', label="Tax Group"),
	'tax_exigibility':fields.selection(selections=
		[('on_invoice', 'Based on Invoice'),
		 ('on_payment', 'Based on Payment'),
		], label='Tax Due', 
		help="Based on Invoice: the tax is due as soon as the invoice is validated.\n"
		"Based on Payment: the tax is due as soon as the payment of the invoice is received."),
	'cash_basis_account':fields.many2one(
		obj='fa.account.template',
		label='Tax Received Account',
		domain=[('deprecated', '=', False)],
		help='Account used as counterpart for the journal entry, for taxes exigible based on payments.')
		}

	_sql_constraints = [
		('name_company_uniq', 'unique(name, company_id, type_tax_use, chart_template_id)', 'Tax names must be unique !'),
	]
	
	_default = {
	'type_tax_use':'sale',
	'amount_type':'percent',
	'active':True,
	'sequence':1,
	'tax_group_id':'on_invoice'
	}

fa_tax_template()

# Fiscal Position Templates

class fa_fiscal_position_template(Model):
	_name = 'fa.fiscal.position.template'
	_description = 'Genaral Model Template for Fiscal Position'
	_columns = {
	'sequence':fields.integer(label='Sequence'),
	'name':fields.varchar(label='Fiscal Position Template', required=True),
	'chart_template_id':fields.many2one(obj='fa.chart.template', label='Chart Template', required=True),
	'account_ids':fields.one2many(obj='fa.fiscal.position.account.template', rel='position_id', label='Account Mapping'),
	'tax_ids':fields.one2many(obj='fa.fiscal.position.tax.template', rel='position_id', label='Tax Mapping'),
	'note':fields.text(label='Note'),
	'auto_apply':fields.boolean(label='Detect Automatically', help="Apply automatically this fiscal position."),
	'vat_required':fields.boolean(label='VAT required', help="Apply only if partner has a VAT number."),
	'country_id':fields.many2one(obj='md.country', label='Country',
		help="Apply only if delivery or invoicing country match."),
	'country_group_id':fields.many2one(obj='md.country.group', label='Country Group',
		help="Apply only if delivery or invocing country match the group."),
	'state_ids':fields.many2many(obj='md.country.states', label='Federal States',rel='fa_fiscal_position_template_state_ids_rel',id1='state_ids',id2='state_id'),
	'zip_from':fields.integer(label='Zip Range From'),
	'zip_to':fields.integer(label='Zip Range To')
	}
	
	_default = {
	'zip_from':0,
	'zip_to':0
	}

fa_fiscal_position_template()

class fa_fiscal_position_tax_template(Model):
	_name = 'fa.fiscal.position.tax.template'
	_description = 'Genaral Model Template Tax Fiscal Position'
	_rec_name = 'position_id'
	_columns = {
	'position_id':fields.many2one(obj='fa.fiscal.position.template', label='Fiscal Position', required=True, on_delete='c'),
	'tax_src_id':fields.many2one(obj='fa.tax.template', label='Tax Source', required=True),
	'tax_dest_id':fields.many2one(obj='fa.tax.template', label='Replacement Tax')
	}

fa_fiscal_position_tax_template()

class fa_fiscal_position_account_template(Model):
	_name = 'fa.fiscal.position.account.template'
	_description = 'Genaral Model Template Account Fiscal Mapping'
	_rec_name = 'position_id'
	_columns = {
	'position_id':fields.many2one(obj='fa.fiscal.position.template', label='Fiscal Mapping', required=True, on_delete='c'),
	'account_src_id':fields.many2one(obj='fa.account.template', label='Account Source', required=True),
	'account_dest_id':fields.many2one(obj='fa.account.template', label='Account Destination', required=True)
	}

fa_fiscal_position_account_template()

class fa_reconcile_model_template(Model):
	_name = "fa.reconcile.model.template"
	_description = 'Genaral Model Reconcile Model Template'
	_columns = {
	'chart_template_id':fields.many2one(obj='fa.chart.template', label='Chart Template', required=True),
	'name':fields.varchar(label='Button Label', required=True),
	'sequence':fields.integer(label='Sequence',required=True),
	'has_second_line':fields.boolean(label='Add a second line'),
	'account_id':fields.many2one(obj='fa.account.template', label='Account', on_delete='c', domain=[('deprecated', '=', False)]),
	'label':fields.varchar(label='Journal Item Label',size=64),
	'amount_type':fields.selection(selections=[
		('fixed', 'Fixed'),
		('percentage', 'Percentage of balance')
		], required=True, label='Amount type'),
	'amount':fields.float(required=True, help="Fixed amount will count as a debit if it is negative, as a credit if it is positive."),
	'tax_id':fields.many2one(obj='fa.tax.template', label='Tax', on_delete='r', domain=[('type_tax_use', '=', 'purchase')]),
	'second_account_id':fields.many2one(obj='fa.account.template', label='Second Account', on_delete='c', domain=[('deprecated', '=', False)]),
	'second_label':fields.varchar(label='Second Journal Item Label',size=64),
	'second_amount_type':fields.selection(selections=[
		('fixed', 'Fixed'),
		('percentage', 'Percentage of amount')
		], label="Second Amount type",required=True),
	'second_amount':fields.float(label='Second Amount', required=True, help="Fixed amount will count as a debit if it is negative, as a credit if it is positive."),
	'second_tax_id':fields.many2one(obj='fa.tax.template', label='Second Tax', on_delete='r', domain=[('type_tax_use', '=', 'purchase')])
	}
	
	_default = {
		'sequence': 10,
		'amount_type':'percentage',
		'second_amount_type':'percentage',
		'amount':100.0,
		'second_amount':100.0
	}

fa_reconcile_model_template()

class fa_accounts_payment_method(Model):
	_name = "fa.accounts.payment.method"
	_description = "Genaral  ModelPayment Methods"
	_columns ={
	'name': fields.varchar(label='Name',required=True, translate=True),
	'code':fields.varchar(label='Code',required=True),  # For internal identification
	'payment_type': fields.selection(label='Payment Type',selections=[('inbound', 'Inbound'), ('outbound', 'Outbound')], required=True)
	}

fa_accounts_payment_method()
