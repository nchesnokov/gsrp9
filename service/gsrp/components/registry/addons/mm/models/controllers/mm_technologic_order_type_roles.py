from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderTypeRoles(ViewModelFindController):
	_name = "find:mm.technologic.order.type.roles"
	_view_name = "mm.technologic.order.type.roles/find"
	_description = "Role Technologic Order Types"

class ViewModelO2MFormMmTechnologicOrderTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.type.roles"
	_view_name = "mm.technologic.order.type.roles/o2m-form"
	_description = "Role Technologic Order Types"

class ViewModelO2MListMmTechnologicOrderTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.type.roles"
	_view_name = "mm.technologic.order.type.roles/o2m-list"
	_description = "Role Technologic Order Types"
