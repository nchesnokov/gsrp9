from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MTreeController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmProductionOrderItems(ViewModelFindController):
	_name = "find:scm.production.order.items"
	_view_name = "scm.production.order.items/find"
	_description = "Production Order Items"

class ViewModelO2MFormScmProductionOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:scm.production.order.items"
	_view_name = "scm.production.order.items/o2m-form"
	_description = "Production Order Items"

class ViewModelO2MTreeScmProductionOrderItems(ViewModelO2MTreeController):
	_name = "o2m-tree:scm.production.order.items"
	_view_name = "scm.production.order.items/o2m-tree"
	_description = "Production Order Items"

class ViewModelO2MListScmProductionOrderItems(ViewModelO2MListController):
	_name = "o2m-list:scm.production.order.items"
	_view_name = "scm.production.order.items/o2m-list"
	_description = "Production Order Items"
