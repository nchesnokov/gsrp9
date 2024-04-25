from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmProductionOrderItemBom(ViewModelFindController):
	_name = "find:scm.production.order.item.bom"
	_view_name = "scm.production.order.item.bom/find"
	_description = "Production Order Items BoM"

class ViewModelO2MFormScmProductionOrderItemBom(ViewModelO2MFormController):
	_name = "o2m-form:scm.production.order.item.bom"
	_view_name = "scm.production.order.item.bom/o2m-form"
	_description = "Production Order Items BoM"

class ViewModelO2MListScmProductionOrderItemBom(ViewModelO2MListController):
	_name = "o2m-list:scm.production.order.item.bom"
	_view_name = "scm.production.order.item.bom/o2m-list"
	_description = "Production Order Items BoM"
