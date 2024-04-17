from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmInvoiceItemRoles(ViewModelFindController):
	_name = "find:crm.invoice.item.roles"
	_view_name = "crm.invoice.item.roles/find"
	_description = "CRM Invoice Item Roles"

class ViewModelO2MFormCrmInvoiceItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.invoice.item.roles"
	_view_name = "crm.invoice.item.roles/o2m-form"
	_description = "CRM Invoice Item Roles"

class ViewModelO2MListCrmInvoiceItemRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.invoice.item.roles"
	_view_name = "crm.invoice.item.roles/o2m-list"
	_description = "CRM Invoice Item Roles"
