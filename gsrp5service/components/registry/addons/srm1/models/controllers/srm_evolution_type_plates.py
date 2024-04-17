from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionTypePlates(ViewModelFindController):
	_name = "find:srm.evolution.type.plates"
	_view_name = "srm.evolution.type.plates/find"
	_description = "SRM Evolution Plates"

class ViewModelO2MFormSrmEvolutionTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.type.plates"
	_view_name = "srm.evolution.type.plates/o2m-form"
	_description = "SRM Evolution Plates"

class ViewModelO2MListSrmEvolutionTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.type.plates"
	_view_name = "srm.evolution.type.plates/o2m-list"
	_description = "SRM Evolution Plates"
