from gsrp5service.orm import fields
from gsrp5service.orm.model import Model, ModelInherit

from decimal import Decimal

from datetime import datetime
from datetime import timedelta

#customize
#Text
class sale_texts(Model):
	_name = 'sale.texts'
	_description = 'General Model Sale Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	}

sale_texts()

class sale_schema_texts(Model):
	_name = 'sale.schema.texts'
	_description = 'General Model Schema Of Sale Texts'
	_rec_name = 'code'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'usage': fields.selection(label='Usage',selections=[('h','Header'),('i','Item'),('b','Both')]),
	'code': fields.varchar(label = 'Code',size=8,translate=True),
	'descr':fields.varchar(label = 'Description',size=128,translate=True),
	'texts': fields.one2many(label='Texts',obj='sale.schema.text.items',rel='schema_id')
	}

sale_schema_texts()

class sale_schema_text_items(Model):
	_name = 'sale.schema.text.items'
	_description = 'General Model Items Of Schema Sale Texts'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'schema_id': fields.many2one(label = 'Schema',obj='sale.schema.texts'),
	'seq': fields.integer(label='Sequence'),
	'text_id': fields.many2one(label = 'Text',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr')
	}

sale_schema_text_items()

# Text end

class sale_order_types(Model):
	_name = 'sale.order.types'
	_description = 'General Model Types Sale Order'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='sale.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='sale.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='sale.order.type.roles',rel='type_id'),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

sale_order_types()

class sale_order_type_roles(Model):
	_name = 'sale.order.type.roles'
	_description = 'General Model Role Sale Order Types'
	_class_model = 'C'
	_class_category = 'order'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='sale.order.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'note': fields.text(label = 'Note')
	}

sale_order_type_roles()

class sale_invoice_types(Model):
	_name = 'sale.invoice.types'
	_description = 'General Model Types Sale Invoice'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'htschema': fields.many2one(label='Text Schema Of Head',obj='sale.schema.texts',domain=[('usage','in',('h','b'))]),
	'itschema': fields.many2one(label='Text Schema Of Item',obj='sale.schema.texts',domain=[('usage','in',('i','b'))]),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.type.roles',rel='type_id'),
	'note': fields.text(label = 'Note')
	}

sale_invoice_types()

class sale_invoice_type_roles(Model):
	_name = 'sale.invoice.type.roles'
	_description = 'General Model Role sale Invoice Types'
	_class_model = 'C'
	_class_category = 'invoice'
	_columns = {
	'type_id': fields.many2one(label = 'Type',obj='sale.invoice.types'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('s','a'))]),
	'required': fields.boolean(label='Required'),
	'note': fields.text(label = 'Note')
	}

sale_invoice_type_roles()

# end customize

class sales_order_categories(Model):
	_name = 'sale.order.categories'
	_description = 'General Model Category Sale Order'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.order.categories'),
	'childs_id': fields.one2many(obj = 'sale.order.categories',rel = 'parent_id',label = 'Childs'),
	'orders': fields.one2many(label='Orders',obj='sale.orders',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sales_order_categories()

class sale_invoice_categories(Model):
	_name = 'sale.invoice.categories'
	_description = 'General Model Category Sale Invoice'
	_columns = {
	'name': fields.varchar(label = 'Name',size=64,translate=True),
	'parent_id': fields.many2one(label='Parent',obj='sale.invoice.categories'),
	'childs_id': fields.one2many(obj = 'sale.invoice.categories',rel = 'parent_id',label = 'Childs'),
	'invoices': fields.one2many(label='Orders',obj='sale.invoices',rel='category_id',limit = 80,readonly=True),
	'note': fields.text(label = 'Note')
	}

sale_invoice_categories()

class sale_orders(Model):
	_name = 'sale.orders'
	_description = 'General Model Sale Orders'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doo'
	_columns = {
	'otype': fields.many2one(label='Type',obj='sale.order.types',on_change='on_change_otype'),
	'category_id': fields.many2one(label='Category',obj='sale.order.categories'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'name': fields.varchar(label = 'Name'),
	'origin': fields.varchar(label = 'Origin'),
	'doo': fields.date(label='Date Of Order',required=True),
	'from_date': fields.date(label='Begin Date Of Order',required=True),
	'to_date': fields.date(label='End Date Of Order',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'recepture': fields.many2one(label='Recepture',obj='md.recepture',domain=[('usage','=','s'),'|',('usage','=','a')],on_change='_on_change_recepture'),
	'items': fields.one2many(label='Items',obj='sale.order.items',rel='order_id'),
	'roles': fields.one2many(label='Roles',obj='sale.order.roles',rel='order_id'),
	'texts': fields.one2many(label='Texts',obj='sale.order.texts',rel='order_id'),
	'payments': fields.one2many(label='Payments',obj='sale.order.payment.schedules',rel='order_id'),
	'note': fields.text('Note')
	}

	def _on_change_otype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('sale.order.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]

	def _on_change_recepture(self,cr,pool,uid,item,context={}):		
		if item['recepture'] and 'name' in item['recepture'] and item['recepture']['name']:
			p = pool.get('md.recepture.output').select(cr,pool,uid,['product','quantity','uom'],[('recepture_id','=',item['recepture']['name'])],context)
			for i in p:
				r = {'delivery_schedules':[{'quantity':i['quantity'],'schedule':datetime.utcnow()+timedelta(3)}]}
				for f in ('product','uom'):
					r[f] = i[f]
				r['price'] = 0.00
				item['items'].append(r)
				
		return None

	_default = {
		'state':'draft'
	}

sale_orders()

class sale_order_texts(Model):
	_name = 'sale.order.texts'
	_description = 'General Model Sale Order Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'order_id': fields.many2one(label='Order',obj='sale.orders'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_order_texts()

class sale_order_roles(Model):
	_name = 'sale.order.roles'
	_description = 'General Model Purchase Order Roles'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_order_roles()

class sale_order_payment_schedules(Model):
	_name = 'sale.order.payment.schedules'
	_description = 'General Model Sale Order Payment Schedules'
	_columns = {
	'order_id': fields.many2one(label = 'Order',obj='sale.orders'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

sale_order_payment_schedules()

class sale_order_items(Model):
	_name = 'sale.order.items'
	_description = 'General Model Sale Order Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'order_id': fields.many2one(obj = 'sale.orders',label = 'Sales Order'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='sale.order.item.delivery.schedules',rel='item_id'),
	'payments': fields.one2many(label='Payments',obj='sale.order.item.payment.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='sale.order.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='sale.order.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.sale.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

sale_order_items()

class sale_order_item_texts(Model):
	_name = 'sale.order.item.texts'
	_description = 'General Model Sale Order Item Texts'
	_class_model = 'C'
	_class_category = 'order'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Item',obj='sale.order.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_order_item_texts()


class sale_order_item_roles(Model):
	_name = 'sale.order.item.roles'
	_description = 'General Model Sale Order Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.order.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_order_item_roles()


class sale_order_item_delivery_schedules(Model):
	_name = 'sale.order.item.delivery.schedules'
	_description = 'General Model Sales Order Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'sale.order.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

sale_order_item_delivery_schedules()

class sale_order_item_payment_schedules(Model):
	_name = 'sale.order.item.payment.schedules'
	_description = 'General Model Sale Order Item Payment Schedules'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.order.items'),
	'amount': fields.numeric(label='Amount',size=(15,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

sale_order_item_payment_schedules()

# Invoice
class sale_invoices(Model):
	_name = 'sale.invoices'
	_description = 'General Model Sale Invoices'
	_inherits = {'common.model':{'_methods':['_calculate_amount_costs']}}
	_date = 'doi'
	_columns = {
	'itype': fields.many2one(label='Type',obj='sale.invoice.types',on_change='on_change_itype'),
	'company_id': fields.many2one(label='Company',obj='md.company'),
	'category_id': fields.many2one(label='Category',obj='sale.invoice.categories'),
	'name': fields.varchar(label = 'Name'),
	'origin': fields.varchar(label = 'Origin'),
	'doi': fields.date(label='Date Of Invoice',required=True),
	'partner': fields.many2one(label='Partner',obj='md.partner',domain=[('iscustomer',)]),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'incoterms1': fields.many2one(label='Incoterms 1',obj='md.incoterms'),
	'incoterms2': fields.varchar(label = 'Incoterms 2'),
	'state': fields.selection(label='State',selections=[('draft','Draft'),('approved','Approved'),('inprocess','In Process'),('closed','Closed'),('canceled','Canceled')]),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_amount_costs'),
	'vat_amount': fields.numeric(label='VAT Amount',size=(15,2),compute='_calculate_amount_costs'),
	'total_amount': fields.numeric(label='Total Amount',size=(15,2),compute='_calculate_amount_costs'),
	'items': fields.one2many(label='Items',obj='sale.invoice.items',rel='invoice_id'),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.roles',rel='invoice_id'),
	'texts': fields.one2many(label='Texts',obj='sale.invoice.texts',rel='invoice_id'),
	'note': fields.text('Note')
	}

	def _on_change_itype(self,cr,pool,uid,item,context={}):		
			roles = pool.get('sale.invoice.type.roles').select(cr,pool.uid,['role_id'],[('type_id','=',item['otype'])],context)
			if len(roles) > 0:
				if 'roles' not in item:
					item['roles'] = []
				for role in roles:
					item[roles].append[role['role_id']]


	_default = {
		'state':'draft'
	}

sale_invoices()

class sale_invoice_texts(Model):
	_name = 'sale.invoice.texts'
	_description = 'General Model Sale Invoce Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'invoice_id': fields.many2one(label='Order',obj='sale.invoices'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_invoice_texts()

class sale_invoice_roles(Model):
	_name = 'sale.invoice.roles'
	_description = 'General Model sale Invoice Roles'
	_columns = {
	'invoice_id': fields.many2one(label = 'Invoice',obj='sale.invoices'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_invoice_roles()

class sales_invoice_items(Model):
	_name = 'sale.invoice.items'
	_description = 'General Model Sales Invoice Items'
	_inherits = {'common.model':{'_methods':['_calculate_items']}}
	_columns = {
	'invoice_id': fields.many2one(obj = 'sale.invoices',label = 'Invoice'),
	'product': fields.many2one(label='Product',obj='md.product',on_change='_on_change_product'	),
	'quantity': fields.numeric(label='Quantity',compute='_calculate_items',size=(13,3)),
	'uom': fields.many2one(label='UoM',obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,3)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'amount': fields.numeric(label='Amount',size=(15,2),compute='_calculate_items'),
	'vat_code': fields.many2one(label='Vat code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'vat_amount': fields.numeric(label='VAT Amount',compute='_calculate_items',size=(15,2)),
	'total_amount': fields.numeric(label='Total Amount',compute='_calculate_items',size=(15,2)),
	'delivery_schedules': fields.one2many(label='Delivery Schedule',obj='sale.invoice.item.delivery.schedules',rel='item_id'),
	'roles': fields.one2many(label='Roles',obj='sale.invoice.item.roles',rel='item_id'),
	'texts': fields.one2many(label='Texts',obj='sale.invoice.item.texts',rel='item_id'),
	'note': fields.text(label = 'Note')
	}

	def _on_change_product(self,cr,pool,uid,item,context={}):		
		if item['product'] and 'name' in item['product'] and item['product']['name']:
			p = pool.get('md.sale.product').select(cr,pool,uid,['vat','uom','price','currency','unit','uop'],[('product_id','=',item['product']['name'])],context)
			if len(p) > 0:
				if item['vat_code'] != p[0]['vat']:
					item['vat_code'] = p[0]['vat']				
				for f in ('uom','price','currency','unit','uop'):
					if item[f] != p[0][f]:
						item[f] = p[0][f]

		return None

	_default = {
		'quantity': 1,
		'unit': 1
	}

sales_invoice_items()

class sale_invoice_item_texts(Model):
	_name = 'sale.invoice.item.texts'
	_description = 'General Model Sale Invoce Item Texts'
	_class_model = 'C'
	_class_category = 'invoice'
	_order_by = "seq asc"
	_sequence = 'seq'
	_columns = {
	'item_id': fields.many2one(label='Order',obj='sale.invoice.items'),
	'seq': fields.integer(label='Sequence',readonly=True,invisible=True),
	'text_id': fields.many2one(label='Text ID',obj='sale.texts'),
	'descr': fields.referenced(ref='text_id.descr'),
	'content':fields.text(label = 'Content',translate=True)
	}

sale_invoice_item_texts()

class sale_invoice_item_roles(Model):
	_name = 'sale.invoice.item.roles'
	_description = 'General Model Purchase Invoice Item Roles'
	_columns = {
	'item_id': fields.many2one(label = 'Item',obj='sale.invoice.items'),
	'role_id': fields.many2one(label = 'Role',obj='md.role.partners',domain=[('trole','in',('c','i','p','a'))]),
	'patner_id': fields.many2one(label = 'Parther',obj='md.partner')
	}

sale_invoice_item_roles()

class sales_invoce_item_delivery_schedules(Model):
	_name = 'sale.invoice.item.delivery.schedules'
	_description = 'General Model Sales Order Item Delivery Schedules'
	_columns = {
	'item_id': fields.many2one(obj = 'sale.invoice.items',label = 'Order Item'),
	'quantity': fields.numeric(label='Quantity',size=(11,3)),
	'schedule': fields.datetime(label='Schedule'),
	'note': fields.text(label = 'Note')
	}

	_default = {
		'quantity': 1.000
	}

sales_invoce_item_delivery_schedules()

#inherit

class md_sale_product(Model):
	_name = 'md.sale.product'
	_description = 'General Model Sale Of Product'
	_columns = {
	'product_id': fields.many2one(label='Product',obj='md.product'),
	'vat': fields.many2one(label='VAT Code',obj='md.vat.code',domain=[('type_vat','in',('s','n'))]),
	'uom': fields.many2one(label="Unit Of Measure",obj='md.uom'),
	'price': fields.numeric(label='Price',size=(13,2)),
	'currency': fields.many2one(label='Currency',obj='md.currency'),
	'unit': fields.integer(label='Unit'),
	'uop': fields.many2one(label="Unit Of Price",obj='md.uom'),
	'note': fields.text(label = 'Note'),
	}

md_sale_product()

class md_sale_product_inherit(ModelInherit):
	_name = 'md.sale.product.inherit'
	_description = 'Genaral Model Inherit For Sale Product'
	_inherit = {'md.product':{'_columns':['sale']},'md.recepture':{'_columns':['usage']}}
	_columns = {
		'sale': fields.one2many(label='Sales',obj='md.sale.product',rel='product_id'),
		'usage': fields.iSelection(selections=[('s','Sale')])
	}
	
md_sale_product_inherit()

