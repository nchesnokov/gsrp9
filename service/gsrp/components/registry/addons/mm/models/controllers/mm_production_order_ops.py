from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderOps(ViewModelFindController):
	_name = "find:mm.production.order.ops"
	_view_name = "mm.production.order.ops/find"
	_description = "Operations of production order"

class ViewModelO2MFormMmProductionOrderOps(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.ops"
	_view_name = "mm.production.order.ops/o2m-form"
	_description = "Operations of production order"

class ViewModelO2MListMmProductionOrderOps(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.ops"
	_view_name = "mm.production.order.ops/o2m-list"
	_description = "Operations of production order"
