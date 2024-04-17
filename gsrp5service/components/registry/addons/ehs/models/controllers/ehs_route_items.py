from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsRouteItems(ViewModelFindController):
	_name = "find:ehs.route.items"
	_view_name = "ehs.route.items/find"
	_description = "Route Items"

class ViewModelO2MFormEhsRouteItems(ViewModelO2MFormController):
	_name = "o2m-form:ehs.route.items"
	_view_name = "ehs.route.items/o2m-form"
	_description = "Route Items"

class ViewModelO2MTreeEhsRouteItems(ViewModelO2MTreeController):
	_name = "o2m-tree:ehs.route.items"
	_view_name = "ehs.route.items/o2m-tree"
	_description = "Route Items"

class ViewModelO2MListEhsRouteItems(ViewModelO2MListController):
	_name = "o2m-list:ehs.route.items"
	_view_name = "ehs.route.items/o2m-list"
	_description = "Route Items"
