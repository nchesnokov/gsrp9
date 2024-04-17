from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmRequestTexts(ViewModelFindController):
	_name = "find:ctrm.request.texts"
	_view_name = "ctrm.request.texts/find"
	_description = "CTRM Request Texts"

class ViewModelO2MFormCtrmRequestTexts(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.request.texts"
	_view_name = "ctrm.request.texts/o2m-form"
	_description = "CTRM Request Texts"

class ViewModelO2MListCtrmRequestTexts(ViewModelO2MListController):
	_name = "o2m-list:ctrm.request.texts"
	_view_name = "ctrm.request.texts/o2m-list"
	_description = "CTRM Request Texts"
