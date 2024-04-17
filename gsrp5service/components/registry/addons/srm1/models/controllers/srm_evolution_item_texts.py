from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionItemTexts(ViewModelFindController):
	_name = "find:srm.evolution.item.texts"
	_view_name = "srm.evolution.item.texts/find"
	_description = "SRM Evolution Item Texts"

class ViewModelO2MFormSrmEvolutionItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.item.texts"
	_view_name = "srm.evolution.item.texts/o2m-form"
	_description = "SRM Evolution Item Texts"

class ViewModelO2MListSrmEvolutionItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.item.texts"
	_view_name = "srm.evolution.item.texts/o2m-list"
	_description = "SRM Evolution Item Texts"
