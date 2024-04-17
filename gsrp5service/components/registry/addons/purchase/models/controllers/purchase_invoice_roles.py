from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoiceRoles(ViewModelFindController):
	_name = "find:purchase.invoice.roles"
	_view_name = "purchase.invoice.roles/find"
	_description = "Purchase Invoice Roles"

class ViewModelO2MFormPurchaseInvoiceRoles(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.roles"
	_view_name = "purchase.invoice.roles/o2m-form"
	_description = "Purchase Invoice Roles"

class ViewModelO2MListPurchaseInvoiceRoles(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.roles"
	_view_name = "purchase.invoice.roles/o2m-list"
	_description = "Purchase Invoice Roles"
