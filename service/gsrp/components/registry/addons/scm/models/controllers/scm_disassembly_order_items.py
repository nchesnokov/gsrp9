from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmDisassemblyOrderItems(ViewModelFindController):
	_name = "find:scm.disassembly.order.items"
	_view_name = "scm.disassembly.order.items/find"
	_description = "Disassembly Order Items"

class ViewModelO2MFormScmDisassemblyOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:scm.disassembly.order.items"
	_view_name = "scm.disassembly.order.items/o2m-form"
	_description = "Disassembly Order Items"

class ViewModelO2MTreeScmDisassemblyOrderItems(ViewModelO2MTreeController):
	_name = "o2m-tree:scm.disassembly.order.items"
	_view_name = "scm.disassembly.order.items/o2m-tree"
	_description = "Disassembly Order Items"

class ViewModelO2MListScmDisassemblyOrderItems(ViewModelO2MListController):
	_name = "o2m-list:scm.disassembly.order.items"
	_view_name = "scm.disassembly.order.items/o2m-list"
	_description = "Disassembly Order Items"
