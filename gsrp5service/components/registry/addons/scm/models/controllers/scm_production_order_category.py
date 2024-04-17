from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchScmProductionOrderCategory(ViewModelSearchController):
	_name = "search:scm.production.order.category"
	_view_name = "scm.production.order.category/search"
	_description = "Category Production Order"

class ViewModelFindScmProductionOrderCategory(ViewModelFindController):
	_name = "find:scm.production.order.category"
	_view_name = "scm.production.order.category/find"
	_description = "Category Production Order"

class ViewModelListScmProductionOrderCategory(ViewModelListController):
	_name = "list:scm.production.order.category"
	_view_name = "scm.production.order.category/list"
	_description = "Category Production Order"

class ViewModelFormModalScmProductionOrderCategory(ViewModelFormModalController):
	_name = "form.modal:scm.production.order.category"
	_view_name = "scm.production.order.category/form.modal"
	_description = "Category Production Order"

class ViewModelFormScmProductionOrderCategory(ViewModelFormController):
	_name = "form:scm.production.order.category"
	_view_name = "scm.production.order.category/form"
	_description = "Category Production Order"

class ViewModelTreeScmProductionOrderCategory(ViewModelTreeController):
	_name = "tree:scm.production.order.category"
	_view_name = "scm.production.order.category/tree"
	_description = "Category Production Order"
