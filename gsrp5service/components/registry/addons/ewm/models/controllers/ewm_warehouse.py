from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchEwmWarehouse(ViewModelSearchController):
	_name = "search:ewm.warehouse"
	_view_name = "ewm.warehouse/search"
	_description = "Warehouse"

class ViewModelFindEwmWarehouse(ViewModelFindController):
	_name = "find:ewm.warehouse"
	_view_name = "ewm.warehouse/find"
	_description = "Warehouse"

class ViewModelListEwmWarehouse(ViewModelListController):
	_name = "list:ewm.warehouse"
	_view_name = "ewm.warehouse/list"
	_description = "Warehouse"

class ViewModelFormModalEwmWarehouse(ViewModelFormModalController):
	_name = "form.modal:ewm.warehouse"
	_view_name = "ewm.warehouse/form.modal"
	_description = "Warehouse"

class ViewModelFormEwmWarehouse(ViewModelFormController):
	_name = "form:ewm.warehouse"
	_view_name = "ewm.warehouse/form"
	_description = "Warehouse"
