from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestItems(ViewModelFindController):
	_name = "find:srm.request.items"
	_view_name = "srm.request.items/find"
	_description = "SRM Request Item"

class ViewModelO2MFormSrmRequestItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.items"
	_view_name = "srm.request.items/o2m-form"
	_description = "SRM Request Item"

class ViewModelO2MListSrmRequestItems(ViewModelO2MListController):
	_name = "o2m-list:srm.request.items"
	_view_name = "srm.request.items/o2m-list"
	_description = "SRM Request Item"
