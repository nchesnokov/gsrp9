from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchEhsRouteCategory(ViewModelSearchController):
	_name = "search:ehs.route.category"
	_view_name = "ehs.route.category/search"
	_description = "Category Route"

class ViewModelFindEhsRouteCategory(ViewModelFindController):
	_name = "find:ehs.route.category"
	_view_name = "ehs.route.category/find"
	_description = "Category Route"

class ViewModelListEhsRouteCategory(ViewModelListController):
	_name = "list:ehs.route.category"
	_view_name = "ehs.route.category/list"
	_description = "Category Route"

class ViewModelFormModalEhsRouteCategory(ViewModelFormModalController):
	_name = "form.modal:ehs.route.category"
	_view_name = "ehs.route.category/form.modal"
	_description = "Category Route"

class ViewModelFormEhsRouteCategory(ViewModelFormController):
	_name = "form:ehs.route.category"
	_view_name = "ehs.route.category/form"
	_description = "Category Route"

class ViewModelTreeEhsRouteCategory(ViewModelTreeController):
	_name = "tree:ehs.route.category"
	_view_name = "ehs.route.category/tree"
	_description = "Category Route"
