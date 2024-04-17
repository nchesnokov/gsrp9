from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseItemTexts(ViewModelFindController):
	_name = "find:srm.response.item.texts"
	_view_name = "srm.response.item.texts/find"
	_description = "SRM Response Item Texts"

class ViewModelO2MFormSrmResponseItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.item.texts"
	_view_name = "srm.response.item.texts/o2m-form"
	_description = "SRM Response Item Texts"

class ViewModelO2MListSrmResponseItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.response.item.texts"
	_view_name = "srm.response.item.texts/o2m-list"
	_description = "SRM Response Item Texts"
