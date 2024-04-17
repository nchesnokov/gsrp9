from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchTrmVehicleCategory(ViewModelSearchController):
	_name = "search:trm.vehicle.category"
	_view_name = "trm.vehicle.category/search"
	_description = "Vehicle Category"

class ViewModelFindTrmVehicleCategory(ViewModelFindController):
	_name = "find:trm.vehicle.category"
	_view_name = "trm.vehicle.category/find"
	_description = "Vehicle Category"

class ViewModelListTrmVehicleCategory(ViewModelListController):
	_name = "list:trm.vehicle.category"
	_view_name = "trm.vehicle.category/list"
	_description = "Vehicle Category"

class ViewModelFormModalTrmVehicleCategory(ViewModelFormModalController):
	_name = "form.modal:trm.vehicle.category"
	_view_name = "trm.vehicle.category/form.modal"
	_description = "Vehicle Category"

class ViewModelFormTrmVehicleCategory(ViewModelFormController):
	_name = "form:trm.vehicle.category"
	_view_name = "trm.vehicle.category/form"
	_description = "Vehicle Category"

class ViewModelTreeTrmVehicleCategory(ViewModelTreeController):
	_name = "tree:trm.vehicle.category"
	_view_name = "trm.vehicle.category/tree"
	_description = "Vehicle Category"
