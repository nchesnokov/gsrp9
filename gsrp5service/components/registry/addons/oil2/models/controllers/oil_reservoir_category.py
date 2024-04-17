from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchOilReservoirCategory(ViewModelSearchController):
	_name = "search:oil.reservoir.category"
	_view_name = "oil.reservoir.category/search"
	_description = "Reservoir Category"

class ViewModelFindOilReservoirCategory(ViewModelFindController):
	_name = "find:oil.reservoir.category"
	_view_name = "oil.reservoir.category/find"
	_description = "Reservoir Category"

class ViewModelListOilReservoirCategory(ViewModelListController):
	_name = "list:oil.reservoir.category"
	_view_name = "oil.reservoir.category/list"
	_description = "Reservoir Category"

class ViewModelFormModalOilReservoirCategory(ViewModelFormModalController):
	_name = "form.modal:oil.reservoir.category"
	_view_name = "oil.reservoir.category/form.modal"
	_description = "Reservoir Category"

class ViewModelFormOilReservoirCategory(ViewModelFormController):
	_name = "form:oil.reservoir.category"
	_view_name = "oil.reservoir.category/form"
	_description = "Reservoir Category"

class ViewModelTreeOilReservoirCategory(ViewModelTreeController):
	_name = "tree:oil.reservoir.category"
	_view_name = "oil.reservoir.category/tree"
	_description = "Reservoir Category"
