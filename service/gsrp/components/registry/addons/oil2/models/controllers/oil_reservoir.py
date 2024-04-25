from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchOilReservoir(ViewModelSearchController):
	_name = "search:oil.reservoir"
	_view_name = "oil.reservoir/search"
	_description = "Reservoir"

class ViewModelFindOilReservoir(ViewModelFindController):
	_name = "find:oil.reservoir"
	_view_name = "oil.reservoir/find"
	_description = "Reservoir"

class ViewModelListOilReservoir(ViewModelListController):
	_name = "list:oil.reservoir"
	_view_name = "oil.reservoir/list"
	_description = "Reservoir"

class ViewModelFormModalOilReservoir(ViewModelFormModalController):
	_name = "form.modal:oil.reservoir"
	_view_name = "oil.reservoir/form.modal"
	_description = "Reservoir"

class ViewModelFormOilReservoir(ViewModelFormController):
	_name = "form:oil.reservoir"
	_view_name = "oil.reservoir/form"
	_description = "Reservoir"
