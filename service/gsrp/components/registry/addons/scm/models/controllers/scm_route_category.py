from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchScmRouteCategory(ViewModelSearchController):
	_name = "search:scm.route.category"
	_view_name = "scm.route.category/search"
	_description = "Category Route"

class ViewModelFindScmRouteCategory(ViewModelFindController):
	_name = "find:scm.route.category"
	_view_name = "scm.route.category/find"
	_description = "Category Route"

class ViewModelListScmRouteCategory(ViewModelListController):
	_name = "list:scm.route.category"
	_view_name = "scm.route.category/list"
	_description = "Category Route"

class ViewModelFormModalScmRouteCategory(ViewModelFormModalController):
	_name = "form.modal:scm.route.category"
	_view_name = "scm.route.category/form.modal"
	_description = "Category Route"

class ViewModelFormScmRouteCategory(ViewModelFormController):
	_name = "form:scm.route.category"
	_view_name = "scm.route.category/form"
	_description = "Category Route"

class ViewModelTreeScmRouteCategory(ViewModelTreeController):
	_name = "tree:scm.route.category"
	_view_name = "scm.route.category/tree"
	_description = "Category Route"
