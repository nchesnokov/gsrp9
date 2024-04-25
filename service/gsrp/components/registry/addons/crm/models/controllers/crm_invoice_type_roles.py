from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmInvoiceTypeRoles(ViewModelFindController):
	_name = "find:crm.invoice.type.roles"
	_view_name = "crm.invoice.type.roles/find"
	_description = "Role CRM Invoice Types"

class ViewModelO2MFormCrmInvoiceTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.invoice.type.roles"
	_view_name = "crm.invoice.type.roles/o2m-form"
	_description = "Role CRM Invoice Types"

class ViewModelO2MListCrmInvoiceTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.invoice.type.roles"
	_view_name = "crm.invoice.type.roles/o2m-list"
	_description = "Role CRM Invoice Types"
