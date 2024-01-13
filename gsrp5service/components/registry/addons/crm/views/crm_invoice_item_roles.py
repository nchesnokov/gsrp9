from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmInvoiceItemRoles(ViewModelFind):
	_name = "model.find.crm.invoice.item.roles"
	_model = "crm.invoice.item.roles"
	_description = "CRM Invoice Item Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmInvoiceItemRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.invoice.item.roles"
	_model = "crm.invoice.item.roles"
	_description = "CRM Invoice Item Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmInvoiceItemRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.invoice.item.roles"
	_model = "crm.invoice.item.roles"
	_description = "CRM Invoice Item Roles"
	_columns = ['item_id', 'role_id', 'patner_id']
