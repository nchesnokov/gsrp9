from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderRoles(ViewModelFindController):
	_name = "find:mm.production.order.roles"
	_view_name = "mm.production.order.roles/find"
	_description = "Production Order Roles"

class ViewModelO2MFormMmProductionOrderRoles(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.roles"
	_view_name = "mm.production.order.roles/o2m-form"
	_description = "Production Order Roles"

class ViewModelO2MListMmProductionOrderRoles(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.roles"
	_view_name = "mm.production.order.roles/o2m-list"
	_description = "Production Order Roles"
