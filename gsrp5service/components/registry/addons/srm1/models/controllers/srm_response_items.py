from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseItems(ViewModelFindController):
	_name = "find:srm.response.items"
	_view_name = "srm.response.items/find"
	_description = "SRM Response Item"

class ViewModelO2MFormSrmResponseItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.items"
	_view_name = "srm.response.items/o2m-form"
	_description = "SRM Response Item"

class ViewModelO2MListSrmResponseItems(ViewModelO2MListController):
	_name = "o2m-list:srm.response.items"
	_view_name = "srm.response.items/o2m-list"
	_description = "SRM Response Item"
