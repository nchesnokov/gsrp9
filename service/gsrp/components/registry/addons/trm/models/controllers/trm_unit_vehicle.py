from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchTrmUnitVehicle(ViewModelSearchController):
	_name = "search:trm.unit.vehicle"
	_view_name = "trm.unit.vehicle/search"
	_description = "Unit Vehicle"

class ViewModelFindTrmUnitVehicle(ViewModelFindController):
	_name = "find:trm.unit.vehicle"
	_view_name = "trm.unit.vehicle/find"
	_description = "Unit Vehicle"

class ViewModelListTrmUnitVehicle(ViewModelListController):
	_name = "list:trm.unit.vehicle"
	_view_name = "trm.unit.vehicle/list"
	_description = "Unit Vehicle"

class ViewModelFormModalTrmUnitVehicle(ViewModelFormModalController):
	_name = "form.modal:trm.unit.vehicle"
	_view_name = "trm.unit.vehicle/form.modal"
	_description = "Unit Vehicle"

class ViewModelFormTrmUnitVehicle(ViewModelFormController):
	_name = "form:trm.unit.vehicle"
	_view_name = "trm.unit.vehicle/form"
	_description = "Unit Vehicle"
