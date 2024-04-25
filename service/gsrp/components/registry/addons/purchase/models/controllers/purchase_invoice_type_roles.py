from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoiceTypeRoles(ViewModelFindController):
	_name = "find:purchase.invoice.type.roles"
	_view_name = "purchase.invoice.type.roles/find"
	_description = "Role Purchase Invoice Types"

class ViewModelO2MFormPurchaseInvoiceTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.type.roles"
	_view_name = "purchase.invoice.type.roles/o2m-form"
	_description = "Role Purchase Invoice Types"

class ViewModelO2MListPurchaseInvoiceTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.type.roles"
	_view_name = "purchase.invoice.type.roles/o2m-list"
	_description = "Role Purchase Invoice Types"
