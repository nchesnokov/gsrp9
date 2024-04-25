from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionTypeItems(ViewModelFindController):
	_name = "find:srm.evolution.type.items"
	_view_name = "srm.evolution.type.items/find"
	_description = "Type of SRM Evolution Items"

class ViewModelO2MFormSrmEvolutionTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.type.items"
	_view_name = "srm.evolution.type.items/o2m-form"
	_description = "Type of SRM Evolution Items"

class ViewModelO2MListSrmEvolutionTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.type.items"
	_view_name = "srm.evolution.type.items/o2m-list"
	_description = "Type of SRM Evolution Items"
