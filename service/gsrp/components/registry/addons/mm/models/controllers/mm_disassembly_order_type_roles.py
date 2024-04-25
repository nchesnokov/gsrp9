from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderTypeRoles(ViewModelFindController):
	_name = "find:mm.disassembly.order.type.roles"
	_view_name = "mm.disassembly.order.type.roles/find"
	_description = "Role Technologic Order Types"

class ViewModelO2MFormMmDisassemblyOrderTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.type.roles"
	_view_name = "mm.disassembly.order.type.roles/o2m-form"
	_description = "Role Technologic Order Types"

class ViewModelO2MListMmDisassemblyOrderTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.type.roles"
	_view_name = "mm.disassembly.order.type.roles/o2m-list"
	_description = "Role Technologic Order Types"
