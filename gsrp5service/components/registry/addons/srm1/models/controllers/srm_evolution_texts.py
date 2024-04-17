from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionTexts(ViewModelFindController):
	_name = "find:srm.evolution.texts"
	_view_name = "srm.evolution.texts/find"
	_description = "SRM Evolution Texts"

class ViewModelO2MFormSrmEvolutionTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.texts"
	_view_name = "srm.evolution.texts/o2m-form"
	_description = "SRM Evolution Texts"

class ViewModelO2MListSrmEvolutionTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.texts"
	_view_name = "srm.evolution.texts/o2m-list"
	_description = "SRM Evolution Texts"
