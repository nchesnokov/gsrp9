from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartItems(ViewModelFindController):
	_name = "find:srm.part.items"
	_view_name = "srm.part.items/find"
	_description = "SRM Part Item"

class ViewModelO2MFormSrmPartItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.items"
	_view_name = "srm.part.items/o2m-form"
	_description = "SRM Part Item"

class ViewModelO2MListSrmPartItems(ViewModelO2MListController):
	_name = "o2m-list:srm.part.items"
	_view_name = "srm.part.items/o2m-list"
	_description = "SRM Part Item"
