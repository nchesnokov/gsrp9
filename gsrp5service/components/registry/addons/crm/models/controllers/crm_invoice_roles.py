from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmInvoiceRoles(ViewModelFindController):
	_name = "find:crm.invoice.roles"
	_view_name = "crm.invoice.roles/find"
	_description = "CRM Invoice Roles"

class ViewModelO2MFormCrmInvoiceRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.invoice.roles"
	_view_name = "crm.invoice.roles/o2m-form"
	_description = "CRM Invoice Roles"

class ViewModelO2MListCrmInvoiceRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.invoice.roles"
	_view_name = "crm.invoice.roles/o2m-list"
	_description = "CRM Invoice Roles"
