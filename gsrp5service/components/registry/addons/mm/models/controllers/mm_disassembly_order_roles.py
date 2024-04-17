from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderRoles(ViewModelFindController):
	_name = "find:mm.disassembly.order.roles"
	_view_name = "mm.disassembly.order.roles/find"
	_description = "Disassembly Order Roles"

class ViewModelO2MFormMmDisassemblyOrderRoles(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.roles"
	_view_name = "mm.disassembly.order.roles/o2m-form"
	_description = "Disassembly Order Roles"

class ViewModelO2MListMmDisassemblyOrderRoles(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.roles"
	_view_name = "mm.disassembly.order.roles/o2m-list"
	_description = "Disassembly Order Roles"
