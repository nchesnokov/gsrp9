from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmProductionOrderCategory(ViewModelSearchController):
	_name = "search:mm.production.order.category"
	_view_name = "mm.production.order.category/search"
	_description = "Category Production Order"

class ViewModelFindMmProductionOrderCategory(ViewModelFindController):
	_name = "find:mm.production.order.category"
	_view_name = "mm.production.order.category/find"
	_description = "Category Production Order"

class ViewModelListMmProductionOrderCategory(ViewModelListController):
	_name = "list:mm.production.order.category"
	_view_name = "mm.production.order.category/list"
	_description = "Category Production Order"

class ViewModelFormModalMmProductionOrderCategory(ViewModelFormModalController):
	_name = "form.modal:mm.production.order.category"
	_view_name = "mm.production.order.category/form.modal"
	_description = "Category Production Order"

class ViewModelFormMmProductionOrderCategory(ViewModelFormController):
	_name = "form:mm.production.order.category"
	_view_name = "mm.production.order.category/form"
	_description = "Category Production Order"

class ViewModelTreeMmProductionOrderCategory(ViewModelTreeController):
	_name = "tree:mm.production.order.category"
	_view_name = "mm.production.order.category/tree"
	_description = "Category Production Order"
