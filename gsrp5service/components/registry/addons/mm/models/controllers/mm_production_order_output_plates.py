from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderOutputPlates(ViewModelFindController):
	_name = "find:mm.production.order.output.plates"
	_view_name = "mm.production.order.output.plates/find"
	_description = "Production Order Output Plates"

class ViewModelO2MFormMmProductionOrderOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.output.plates"
	_view_name = "mm.production.order.output.plates/o2m-form"
	_description = "Production Order Output Plates"

class ViewModelO2MKanbanMmProductionOrderOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:mm.production.order.output.plates"
	_view_name = "mm.production.order.output.plates/o2m-kanban"
	_description = "Production Order Output Plates"

class ViewModelO2MListMmProductionOrderOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.output.plates"
	_view_name = "mm.production.order.output.plates/o2m-list"
	_description = "Production Order Output Plates"
