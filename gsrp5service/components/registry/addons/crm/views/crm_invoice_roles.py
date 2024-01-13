from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmInvoiceRoles(ViewModelFind):
	_name = "model.find.crm.invoice.roles"
	_model = "crm.invoice.roles"
	_description = "CRM Invoice Roles"
	_columns = ['invoice_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmInvoiceRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.roles"
	_model = "crm.invoice.roles"
	_description = "CRM Invoice Roles"
	_columns = ['invoice_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmInvoiceRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.roles"
	_model = "crm.invoice.roles"
	_description = "CRM Invoice Roles"
	_columns = ['invoice_id', 'role_id', 'patner_id']
