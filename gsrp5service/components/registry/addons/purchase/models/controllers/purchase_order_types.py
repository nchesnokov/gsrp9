from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseOrderTypes(ViewModelSearchController):
	_name = "search:purchase.order.types"
	_view_name = "purchase.order.types/search"
	_description = "Types Purchase Order"

class ViewModelFindPurchaseOrderTypes(ViewModelFindController):
	_name = "find:purchase.order.types"
	_view_name = "purchase.order.types/find"
	_description = "Types Purchase Order"

class ViewModelListPurchaseOrderTypes(ViewModelListController):
	_name = "list:purchase.order.types"
	_view_name = "purchase.order.types/list"
	_description = "Types Purchase Order"

class ViewModelFormModalPurchaseOrderTypes(ViewModelFormModalController):
	_name = "form.modal:purchase.order.types"
	_view_name = "purchase.order.types/form.modal"
	_description = "Types Purchase Order"

class ViewModelFormPurchaseOrderTypes(ViewModelFormController):
	_name = "form:purchase.order.types"
	_view_name = "purchase.order.types/form"
	_description = "Types Purchase Order"
