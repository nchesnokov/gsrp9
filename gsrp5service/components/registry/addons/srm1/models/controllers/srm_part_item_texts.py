from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartItemTexts(ViewModelFindController):
	_name = "find:srm.part.item.texts"
	_view_name = "srm.part.item.texts/find"
	_description = "SRM Part Item Texts"

class ViewModelO2MFormSrmPartItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.item.texts"
	_view_name = "srm.part.item.texts/o2m-form"
	_description = "SRM Part Item Texts"

class ViewModelO2MListSrmPartItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.part.item.texts"
	_view_name = "srm.part.item.texts/o2m-list"
	_description = "SRM Part Item Texts"
