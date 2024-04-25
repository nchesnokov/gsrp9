from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmRequestItemTexts(ViewModelFindController):
	_name = "find:ctrm.request.item.texts"
	_view_name = "ctrm.request.item.texts/find"
	_description = "CTRM Request Item Texts"

class ViewModelO2MFormCtrmRequestItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.request.item.texts"
	_view_name = "ctrm.request.item.texts/o2m-form"
	_description = "CTRM Request Item Texts"

class ViewModelO2MListCtrmRequestItemTexts(ViewModelO2MListController):
	_name = "o2m-list:ctrm.request.item.texts"
	_view_name = "ctrm.request.item.texts/o2m-list"
	_description = "CTRM Request Item Texts"
