from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionItemOutputPlates(ViewModelFindController):
	_name = "find:srm.evolution.item.output.plates"
	_view_name = "srm.evolution.item.output.plates/find"
	_description = "Evolution Item Output Plates"

class ViewModelO2MFormSrmEvolutionItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.item.output.plates"
	_view_name = "srm.evolution.item.output.plates/o2m-form"
	_description = "Evolution Item Output Plates"

class ViewModelO2MKanbanSrmEvolutionItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.evolution.item.output.plates"
	_view_name = "srm.evolution.item.output.plates/o2m-kanban"
	_description = "Evolution Item Output Plates"

class ViewModelO2MListSrmEvolutionItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.item.output.plates"
	_view_name = "srm.evolution.item.output.plates/o2m-list"
	_description = "Evolution Item Output Plates"
