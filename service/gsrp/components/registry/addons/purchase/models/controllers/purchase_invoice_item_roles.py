from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoiceItemRoles(ViewModelFindController):
	_name = "find:purchase.invoice.item.roles"
	_view_name = "purchase.invoice.item.roles/find"
	_description = "Purchase Invoice Item Roles"

class ViewModelO2MFormPurchaseInvoiceItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.item.roles"
	_view_name = "purchase.invoice.item.roles/o2m-form"
	_description = "Purchase Invoice Item Roles"

class ViewModelO2MListPurchaseInvoiceItemRoles(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.item.roles"
	_view_name = "purchase.invoice.item.roles/o2m-list"
	_description = "Purchase Invoice Item Roles"
