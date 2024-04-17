from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderRoles(ViewModelFindController):
	_name = "find:mm.technologic.order.roles"
	_view_name = "mm.technologic.order.roles/find"
	_description = "Technologic Order Roles"

class ViewModelO2MFormMmTechnologicOrderRoles(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.roles"
	_view_name = "mm.technologic.order.roles/o2m-form"
	_description = "Technologic Order Roles"

class ViewModelO2MListMmTechnologicOrderRoles(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.roles"
	_view_name = "mm.technologic.order.roles/o2m-list"
	_description = "Technologic Order Roles"
