from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderItems(ViewModelFindController):
	_name = "find:mm.production.order.items"
	_view_name = "mm.production.order.items/find"
	_description = "Production Order Items"

class ViewModelO2MFormMmProductionOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.items"
	_view_name = "mm.production.order.items/o2m-form"
	_description = "Production Order Items"

class ViewModelO2MListMmProductionOrderItems(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.items"
	_view_name = "mm.production.order.items/o2m-list"
	_description = "Production Order Items"
