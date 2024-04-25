from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRouteItems(ViewModelFindController):
	_name = "find:srm.route.items"
	_view_name = "srm.route.items/find"
	_description = "SRM Route Items"

class ViewModelO2MFormSrmRouteItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.route.items"
	_view_name = "srm.route.items/o2m-form"
	_description = "SRM Route Items"

class ViewModelO2MListSrmRouteItems(ViewModelO2MListController):
	_name = "o2m-list:srm.route.items"
	_view_name = "srm.route.items/o2m-list"
	_description = "SRM Route Items"
