from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsProductionOrderItems(ViewModelFindController):
	_name = "find:ehs.production.order.items"
	_view_name = "ehs.production.order.items/find"
	_description = "Production Order Items"

class ViewModelO2MFormEhsProductionOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:ehs.production.order.items"
	_view_name = "ehs.production.order.items/o2m-form"
	_description = "Production Order Items"

class ViewModelO2MTreeEhsProductionOrderItems(ViewModelO2MTreeController):
	_name = "o2m-tree:ehs.production.order.items"
	_view_name = "ehs.production.order.items/o2m-tree"
	_description = "Production Order Items"

class ViewModelO2MListEhsProductionOrderItems(ViewModelO2MListController):
	_name = "o2m-list:ehs.production.order.items"
	_view_name = "ehs.production.order.items/o2m-list"
	_description = "Production Order Items"
