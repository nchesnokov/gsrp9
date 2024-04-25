from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandOutputPlates(ViewModelFindController):
	_name = "find:mrp.demand.output.plates"
	_view_name = "mrp.demand.output.plates/find"
	_description = "MRP Demand Output Plates"

class ViewModelO2MFormMrpDemandOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.output.plates"
	_view_name = "mrp.demand.output.plates/o2m-form"
	_description = "MRP Demand Output Plates"

class ViewModelO2MKanbanMrpDemandOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:mrp.demand.output.plates"
	_view_name = "mrp.demand.output.plates/o2m-kanban"
	_description = "MRP Demand Output Plates"

class ViewModelO2MListMrpDemandOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.output.plates"
	_view_name = "mrp.demand.output.plates/o2m-list"
	_description = "MRP Demand Output Plates"
