from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmMapOps(ViewModelSearchController):
	_name = "search:mm.map.ops"
	_view_name = "mm.map.ops/search"
	_description = "Operation of map"

class ViewModelFindMmMapOps(ViewModelFindController):
	_name = "find:mm.map.ops"
	_view_name = "mm.map.ops/find"
	_description = "Operation of map"

class ViewModelListMmMapOps(ViewModelListController):
	_name = "list:mm.map.ops"
	_view_name = "mm.map.ops/list"
	_description = "Operation of map"

class ViewModelFormModalMmMapOps(ViewModelFormModalController):
	_name = "form.modal:mm.map.ops"
	_view_name = "mm.map.ops/form.modal"
	_description = "Operation of map"

class ViewModelFormMmMapOps(ViewModelFormController):
	_name = "form:mm.map.ops"
	_view_name = "mm.map.ops/form"
	_description = "Operation of map"
