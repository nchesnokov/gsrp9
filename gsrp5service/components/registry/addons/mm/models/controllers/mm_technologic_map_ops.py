from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicMapOps(ViewModelFindController):
	_name = "find:mm.technologic.map.ops"
	_view_name = "mm.technologic.map.ops/find"
	_description = "Operations of technology map"

class ViewModelO2MFormMmTechnologicMapOps(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.map.ops"
	_view_name = "mm.technologic.map.ops/o2m-form"
	_description = "Operations of technology map"

class ViewModelO2MListMmTechnologicMapOps(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.map.ops"
	_view_name = "mm.technologic.map.ops/o2m-list"
	_description = "Operations of technology map"
