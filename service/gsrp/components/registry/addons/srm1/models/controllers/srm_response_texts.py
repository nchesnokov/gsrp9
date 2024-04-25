from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseTexts(ViewModelFindController):
	_name = "find:srm.response.texts"
	_view_name = "srm.response.texts/find"
	_description = "SRM Response Texts"

class ViewModelO2MFormSrmResponseTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.texts"
	_view_name = "srm.response.texts/o2m-form"
	_description = "SRM Response Texts"

class ViewModelO2MListSrmResponseTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.response.texts"
	_view_name = "srm.response.texts/o2m-list"
	_description = "SRM Response Texts"
