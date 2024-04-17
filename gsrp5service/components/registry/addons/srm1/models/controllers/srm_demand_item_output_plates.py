from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandItemOutputPlates(ViewModelFindController):
	_name = "find:srm.demand.item.output.plates"
	_view_name = "srm.demand.item.output.plates/find"
	_description = "Demand Item Output Plates"

class ViewModelO2MFormSrmDemandItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.item.output.plates"
	_view_name = "srm.demand.item.output.plates/o2m-form"
	_description = "Demand Item Output Plates"

class ViewModelO2MKanbanSrmDemandItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.demand.item.output.plates"
	_view_name = "srm.demand.item.output.plates/o2m-kanban"
	_description = "Demand Item Output Plates"

class ViewModelO2MListSrmDemandItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.item.output.plates"
	_view_name = "srm.demand.item.output.plates/o2m-list"
	_description = "Demand Item Output Plates"
