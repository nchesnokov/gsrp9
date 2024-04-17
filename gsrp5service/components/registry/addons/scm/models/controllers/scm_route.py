from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchScmRoute(ViewModelSearchController):
	_name = "search:scm.route"
	_view_name = "scm.route/search"
	_description = "Route"

class ViewModelFindScmRoute(ViewModelFindController):
	_name = "find:scm.route"
	_view_name = "scm.route/find"
	_description = "Route"

class ViewModelListScmRoute(ViewModelListController):
	_name = "list:scm.route"
	_view_name = "scm.route/list"
	_description = "Route"

class ViewModelFormModalScmRoute(ViewModelFormModalController):
	_name = "form.modal:scm.route"
	_view_name = "scm.route/form.modal"
	_description = "Route"

class ViewModelFormScmRoute(ViewModelFormController):
	_name = "form:scm.route"
	_view_name = "scm.route/form"
	_description = "Route"
