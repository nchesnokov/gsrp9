from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchTmLocations(ViewModelSearchController):
	_name = "search:tm.locations"
	_view_name = "tm.locations/search"
	_description = "Locations"

class ViewModelFindTmLocations(ViewModelFindController):
	_name = "find:tm.locations"
	_view_name = "tm.locations/find"
	_description = "Locations"

class ViewModelListTmLocations(ViewModelListController):
	_name = "list:tm.locations"
	_view_name = "tm.locations/list"
	_description = "Locations"

class ViewModelFormModalTmLocations(ViewModelFormModalController):
	_name = "form.modal:tm.locations"
	_view_name = "tm.locations/form.modal"
	_description = "Locations"

class ViewModelFormTmLocations(ViewModelFormController):
	_name = "form:tm.locations"
	_view_name = "tm.locations/form"
	_description = "Locations"

class ViewModelTreeTmLocations(ViewModelTreeController):
	_name = "tree:tm.locations"
	_view_name = "tm.locations/tree"
	_description = "Locations"
