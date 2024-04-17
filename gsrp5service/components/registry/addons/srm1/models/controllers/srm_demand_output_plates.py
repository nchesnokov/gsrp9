from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandOutputPlates(ViewModelFindController):
	_name = "find:srm.demand.output.plates"
	_view_name = "srm.demand.output.plates/find"
	_description = "SRM Demand Output Plates"

class ViewModelO2MFormSrmDemandOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.output.plates"
	_view_name = "srm.demand.output.plates/o2m-form"
	_description = "SRM Demand Output Plates"

class ViewModelO2MKanbanSrmDemandOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.demand.output.plates"
	_view_name = "srm.demand.output.plates/o2m-kanban"
	_description = "SRM Demand Output Plates"

class ViewModelO2MListSrmDemandOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.output.plates"
	_view_name = "srm.demand.output.plates/o2m-list"
	_description = "SRM Demand Output Plates"
