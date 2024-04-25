from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchEhsProductionOrderCategory(ViewModelSearchController):
	_name = "search:ehs.production.order.category"
	_view_name = "ehs.production.order.category/search"
	_description = "Category Production Order"

class ViewModelFindEhsProductionOrderCategory(ViewModelFindController):
	_name = "find:ehs.production.order.category"
	_view_name = "ehs.production.order.category/find"
	_description = "Category Production Order"

class ViewModelListEhsProductionOrderCategory(ViewModelListController):
	_name = "list:ehs.production.order.category"
	_view_name = "ehs.production.order.category/list"
	_description = "Category Production Order"

class ViewModelFormModalEhsProductionOrderCategory(ViewModelFormModalController):
	_name = "form.modal:ehs.production.order.category"
	_view_name = "ehs.production.order.category/form.modal"
	_description = "Category Production Order"

class ViewModelFormEhsProductionOrderCategory(ViewModelFormController):
	_name = "form:ehs.production.order.category"
	_view_name = "ehs.production.order.category/form"
	_description = "Category Production Order"

class ViewModelTreeEhsProductionOrderCategory(ViewModelTreeController):
	_name = "tree:ehs.production.order.category"
	_view_name = "ehs.production.order.category/tree"
	_description = "Category Production Order"
