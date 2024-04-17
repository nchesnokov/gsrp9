from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionItems(ViewModelFindController):
	_name = "find:srm.evolution.items"
	_view_name = "srm.evolution.items/find"
	_description = "SRM Evolution Item"

class ViewModelO2MFormSrmEvolutionItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.items"
	_view_name = "srm.evolution.items/o2m-form"
	_description = "SRM Evolution Item"

class ViewModelO2MListSrmEvolutionItems(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.items"
	_view_name = "srm.evolution.items/o2m-list"
	_description = "SRM Evolution Item"
