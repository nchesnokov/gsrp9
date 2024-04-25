from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmRouteItems(ViewModelFindController):
	_name = "find:scm.route.items"
	_view_name = "scm.route.items/find"
	_description = "Route Items"

class ViewModelO2MFormScmRouteItems(ViewModelO2MFormController):
	_name = "o2m-form:scm.route.items"
	_view_name = "scm.route.items/o2m-form"
	_description = "Route Items"

class ViewModelO2MTreeScmRouteItems(ViewModelO2MTreeController):
	_name = "o2m-tree:scm.route.items"
	_view_name = "scm.route.items/o2m-tree"
	_description = "Route Items"

class ViewModelO2MListScmRouteItems(ViewModelO2MListController):
	_name = "o2m-list:scm.route.items"
	_view_name = "scm.route.items/o2m-list"
	_description = "Route Items"
