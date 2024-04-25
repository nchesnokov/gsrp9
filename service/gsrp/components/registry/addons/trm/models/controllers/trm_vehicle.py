from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchTrmVehicle(ViewModelSearchController):
	_name = "search:trm.vehicle"
	_view_name = "trm.vehicle/search"
	_description = "Vehicle"

class ViewModelFindTrmVehicle(ViewModelFindController):
	_name = "find:trm.vehicle"
	_view_name = "trm.vehicle/find"
	_description = "Vehicle"

class ViewModelListTrmVehicle(ViewModelListController):
	_name = "list:trm.vehicle"
	_view_name = "trm.vehicle/list"
	_description = "Vehicle"

class ViewModelFormModalTrmVehicle(ViewModelFormModalController):
	_name = "form.modal:trm.vehicle"
	_view_name = "trm.vehicle/form.modal"
	_description = "Vehicle"

class ViewModelFormTrmVehicle(ViewModelFormController):
	_name = "form:trm.vehicle"
	_view_name = "trm.vehicle/form"
	_description = "Vehicle"
