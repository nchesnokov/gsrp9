from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyMapOps(ViewModelFindController):
	_name = "find:mm.disassembly.map.ops"
	_view_name = "mm.disassembly.map.ops/find"
	_description = "Operations of disassembly map"

class ViewModelO2MFormMmDisassemblyMapOps(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.map.ops"
	_view_name = "mm.disassembly.map.ops/o2m-form"
	_description = "Operations of disassembly map"

class ViewModelO2MListMmDisassemblyMapOps(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.map.ops"
	_view_name = "mm.disassembly.map.ops/o2m-list"
	_description = "Operations of disassembly map"
