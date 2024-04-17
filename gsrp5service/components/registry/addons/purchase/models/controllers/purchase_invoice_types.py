from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseInvoiceTypes(ViewModelSearchController):
	_name = "search:purchase.invoice.types"
	_view_name = "purchase.invoice.types/search"
	_description = "Types Purchase Invoice"

class ViewModelFindPurchaseInvoiceTypes(ViewModelFindController):
	_name = "find:purchase.invoice.types"
	_view_name = "purchase.invoice.types/find"
	_description = "Types Purchase Invoice"

class ViewModelListPurchaseInvoiceTypes(ViewModelListController):
	_name = "list:purchase.invoice.types"
	_view_name = "purchase.invoice.types/list"
	_description = "Types Purchase Invoice"

class ViewModelFormModalPurchaseInvoiceTypes(ViewModelFormModalController):
	_name = "form.modal:purchase.invoice.types"
	_view_name = "purchase.invoice.types/form.modal"
	_description = "Types Purchase Invoice"

class ViewModelFormPurchaseInvoiceTypes(ViewModelFormController):
	_name = "form:purchase.invoice.types"
	_view_name = "purchase.invoice.types/form"
	_description = "Types Purchase Invoice"
