from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoiceItems(ViewModelFindController):
	_name = "find:purchase.invoice.items"
	_view_name = "purchase.invoice.items/find"
	_description = "Purchase Invoice Items"

class ViewModelO2MFormPurchaseInvoiceItems(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.items"
	_view_name = "purchase.invoice.items/o2m-form"
	_description = "Purchase Invoice Items"

class ViewModelO2MListPurchaseInvoiceItems(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.items"
	_view_name = "purchase.invoice.items/o2m-list"
	_description = "Purchase Invoice Items"
