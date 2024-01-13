from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmInvoiceTypeRoles(ViewModelFind):
	_name = "model.find.crm.invoice.type.roles"
	_model = "crm.invoice.type.roles"
	_description = "Role CRM Invoice Types"
	_columns = ['type_id', 'role_id', 'required']

class ViewModelO2MFormCrmInvoiceTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.type.roles"
	_model = "crm.invoice.type.roles"
	_description = "Role CRM Invoice Types"
	_columns = ['type_id', 'role_id', 'required', 'note']

class ViewModelO2MListCrmInvoiceTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.type.roles"
	_model = "crm.invoice.type.roles"
	_description = "Role CRM Invoice Types"
	_columns = ['type_id', 'role_id', 'required']
