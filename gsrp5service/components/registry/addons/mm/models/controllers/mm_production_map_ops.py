from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionMapOps(ViewModelFindController):
	_name = "find:mm.production.map.ops"
	_view_name = "mm.production.map.ops/find"
	_description = "Operations of production map"

class ViewModelO2MFormMmProductionMapOps(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.map.ops"
	_view_name = "mm.production.map.ops/o2m-form"
	_description = "Operations of production map"

class ViewModelO2MListMmProductionMapOps(ViewModelO2MListController):
	_name = "o2m-list:mm.production.map.ops"
	_view_name = "mm.production.map.ops/o2m-list"
	_description = "Operations of production map"
