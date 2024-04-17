from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmDisassemblyOrderItemMob(ViewModelFindController):
	_name = "find:scm.disassembly.order.item.mob"
	_view_name = "scm.disassembly.order.item.mob/find"
	_description = "Disassembly Order Items MoB"

class ViewModelO2MFormScmDisassemblyOrderItemMob(ViewModelO2MFormController):
	_name = "o2m-form:scm.disassembly.order.item.mob"
	_view_name = "scm.disassembly.order.item.mob/o2m-form"
	_description = "Disassembly Order Items MoB"

class ViewModelO2MListScmDisassemblyOrderItemMob(ViewModelO2MListController):
	_name = "o2m-list:scm.disassembly.order.item.mob"
	_view_name = "scm.disassembly.order.item.mob/o2m-list"
	_description = "Disassembly Order Items MoB"
