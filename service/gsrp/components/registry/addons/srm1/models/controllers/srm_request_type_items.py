from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestTypeItems(ViewModelFindController):
	_name = "find:srm.request.type.items"
	_view_name = "srm.request.type.items/find"
	_description = "Type of SRM Request Items"

class ViewModelO2MFormSrmRequestTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.type.items"
	_view_name = "srm.request.type.items/o2m-form"
	_description = "Type of SRM Request Items"

class ViewModelO2MListSrmRequestTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.request.type.items"
	_view_name = "srm.request.type.items/o2m-list"
	_description = "Type of SRM Request Items"
