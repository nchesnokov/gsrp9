from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionOutputPlates(ViewModelFindController):
	_name = "find:srm.evolution.output.plates"
	_view_name = "srm.evolution.output.plates/find"
	_description = "SRM Evolution Output Plates"

class ViewModelO2MFormSrmEvolutionOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.output.plates"
	_view_name = "srm.evolution.output.plates/o2m-form"
	_description = "SRM Evolution Output Plates"

class ViewModelO2MKanbanSrmEvolutionOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.evolution.output.plates"
	_view_name = "srm.evolution.output.plates/o2m-kanban"
	_description = "SRM Evolution Output Plates"

class ViewModelO2MListSrmEvolutionOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.output.plates"
	_view_name = "srm.evolution.output.plates/o2m-list"
	_description = "SRM Evolution Output Plates"
