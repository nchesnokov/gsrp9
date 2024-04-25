from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestItemTexts(ViewModelFindController):
	_name = "find:srm.request.item.texts"
	_view_name = "srm.request.item.texts/find"
	_description = "SRM Request Item Texts"

class ViewModelO2MFormSrmRequestItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.item.texts"
	_view_name = "srm.request.item.texts/o2m-form"
	_description = "SRM Request Item Texts"

class ViewModelO2MListSrmRequestItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.request.item.texts"
	_view_name = "srm.request.item.texts/o2m-list"
	_description = "SRM Request Item Texts"
