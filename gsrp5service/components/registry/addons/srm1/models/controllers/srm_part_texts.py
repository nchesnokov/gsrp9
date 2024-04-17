from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartTexts(ViewModelFindController):
	_name = "find:srm.part.texts"
	_view_name = "srm.part.texts/find"
	_description = "SRM Part Texts"

class ViewModelO2MFormSrmPartTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.texts"
	_view_name = "srm.part.texts/o2m-form"
	_description = "SRM Part Texts"

class ViewModelO2MListSrmPartTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.part.texts"
	_view_name = "srm.part.texts/o2m-list"
	_description = "SRM Part Texts"
