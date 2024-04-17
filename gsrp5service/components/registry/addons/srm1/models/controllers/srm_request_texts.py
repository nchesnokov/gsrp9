from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestTexts(ViewModelFindController):
	_name = "find:srm.request.texts"
	_view_name = "srm.request.texts/find"
	_description = "SRM Request Texts"

class ViewModelO2MFormSrmRequestTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.texts"
	_view_name = "srm.request.texts/o2m-form"
	_description = "SRM Request Texts"

class ViewModelO2MListSrmRequestTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.request.texts"
	_view_name = "srm.request.texts/o2m-list"
	_description = "SRM Request Texts"
