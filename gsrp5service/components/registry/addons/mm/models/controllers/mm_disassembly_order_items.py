from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderItems(ViewModelFindController):
	_name = "find:mm.disassembly.order.items"
	_view_name = "mm.disassembly.order.items/find"
	_description = "Disassembly Order Items"

class ViewModelO2MFormMmDisassemblyOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.items"
	_view_name = "mm.disassembly.order.items/o2m-form"
	_description = "Disassembly Order Items"

class ViewModelO2MListMmDisassemblyOrderItems(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.items"
	_view_name = "mm.disassembly.order.items/o2m-list"
	_description = "Disassembly Order Items"
