from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderTypeRoles(ViewModelFindController):
	_name = "find:mm.production.order.type.roles"
	_view_name = "mm.production.order.type.roles/find"
	_description = "Role Production Order Types"

class ViewModelO2MFormMmProductionOrderTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.type.roles"
	_view_name = "mm.production.order.type.roles/o2m-form"
	_description = "Role Production Order Types"

class ViewModelO2MListMmProductionOrderTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.type.roles"
	_view_name = "mm.production.order.type.roles/o2m-list"
	_description = "Role Production Order Types"
