from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsDisassemblyOrderItemMob(ViewModelFindController):
	_name = "find:ehs.disassembly.order.item.mob"
	_view_name = "ehs.disassembly.order.item.mob/find"
	_description = "Disassembly Order Items MoB"

class ViewModelO2MFormEhsDisassemblyOrderItemMob(ViewModelO2MFormController):
	_name = "o2m-form:ehs.disassembly.order.item.mob"
	_view_name = "ehs.disassembly.order.item.mob/o2m-form"
	_description = "Disassembly Order Items MoB"

class ViewModelO2MListEhsDisassemblyOrderItemMob(ViewModelO2MListController):
	_name = "o2m-list:ehs.disassembly.order.item.mob"
	_view_name = "ehs.disassembly.order.item.mob/o2m-list"
	_description = "Disassembly Order Items MoB"
