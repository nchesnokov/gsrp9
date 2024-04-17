from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchWkfLocations(ViewModelSearchController):
	_name = "search:wkf.locations"
	_view_name = "wkf.locations/search"
	_description = "WKF Location"

class ViewModelFindWkfLocations(ViewModelFindController):
	_name = "find:wkf.locations"
	_view_name = "wkf.locations/find"
	_description = "WKF Location"

class ViewModelListWkfLocations(ViewModelListController):
	_name = "list:wkf.locations"
	_view_name = "wkf.locations/list"
	_description = "WKF Location"

class ViewModelFormModalWkfLocations(ViewModelFormModalController):
	_name = "form.modal:wkf.locations"
	_view_name = "wkf.locations/form.modal"
	_description = "WKF Location"

class ViewModelFormWkfLocations(ViewModelFormController):
	_name = "form:wkf.locations"
	_view_name = "wkf.locations/form"
	_description = "WKF Location"

class ViewModelTreeWkfLocations(ViewModelTreeController):
	_name = "tree:wkf.locations"
	_view_name = "wkf.locations/tree"
	_description = "WKF Location"
