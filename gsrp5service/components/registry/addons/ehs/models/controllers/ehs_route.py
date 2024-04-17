from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchEhsRoute(ViewModelSearchController):
	_name = "search:ehs.route"
	_view_name = "ehs.route/search"
	_description = "Route"

class ViewModelFindEhsRoute(ViewModelFindController):
	_name = "find:ehs.route"
	_view_name = "ehs.route/find"
	_description = "Route"

class ViewModelListEhsRoute(ViewModelListController):
	_name = "list:ehs.route"
	_view_name = "ehs.route/list"
	_description = "Route"

class ViewModelFormModalEhsRoute(ViewModelFormModalController):
	_name = "form.modal:ehs.route"
	_view_name = "ehs.route/form.modal"
	_description = "Route"

class ViewModelFormEhsRoute(ViewModelFormController):
	_name = "form:ehs.route"
	_view_name = "ehs.route/form"
	_description = "Route"
