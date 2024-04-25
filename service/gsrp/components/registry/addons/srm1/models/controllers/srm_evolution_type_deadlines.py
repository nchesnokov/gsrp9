from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionTypeDeadlines(ViewModelFindController):
	_name = "find:srm.evolution.type.deadlines"
	_view_name = "srm.evolution.type.deadlines/find"
	_description = "Deadlines SRM Evolution Types"

class ViewModelO2MFormSrmEvolutionTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.type.deadlines"
	_view_name = "srm.evolution.type.deadlines/o2m-form"
	_description = "Deadlines SRM Evolution Types"

class ViewModelO2MListSrmEvolutionTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.type.deadlines"
	_view_name = "srm.evolution.type.deadlines/o2m-list"
	_description = "Deadlines SRM Evolution Types"
