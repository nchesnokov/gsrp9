from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsDisassemblyOrderItems(ViewModelFindController):
	_name = "find:ehs.disassembly.order.items"
	_view_name = "ehs.disassembly.order.items/find"
	_description = "Disassembly Order Items"

class ViewModelO2MFormEhsDisassemblyOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:ehs.disassembly.order.items"
	_view_name = "ehs.disassembly.order.items/o2m-form"
	_description = "Disassembly Order Items"

class ViewModelO2MTreeEhsDisassemblyOrderItems(ViewModelO2MTreeController):
	_name = "o2m-tree:ehs.disassembly.order.items"
	_view_name = "ehs.disassembly.order.items/o2m-tree"
	_description = "Disassembly Order Items"

class ViewModelO2MListEhsDisassemblyOrderItems(ViewModelO2MListController):
	_name = "o2m-list:ehs.disassembly.order.items"
	_view_name = "ehs.disassembly.order.items/o2m-list"
	_description = "Disassembly Order Items"
