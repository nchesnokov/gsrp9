from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderOps(ViewModelFindController):
	_name = "find:mm.disassembly.order.ops"
	_view_name = "mm.disassembly.order.ops/find"
	_description = "Operations of disassembly order"

class ViewModelO2MFormMmDisassemblyOrderOps(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.ops"
	_view_name = "mm.disassembly.order.ops/o2m-form"
	_description = "Operations of disassembly order"

class ViewModelO2MListMmDisassemblyOrderOps(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.ops"
	_view_name = "mm.disassembly.order.ops/o2m-list"
	_description = "Operations of disassembly order"
