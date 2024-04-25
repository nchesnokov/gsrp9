from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartTypeItems(ViewModelFindController):
	_name = "find:srm.part.type.items"
	_view_name = "srm.part.type.items/find"
	_description = "Type of SRM Part Items"

class ViewModelO2MFormSrmPartTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.type.items"
	_view_name = "srm.part.type.items/o2m-form"
	_description = "Type of SRM Part Items"

class ViewModelO2MListSrmPartTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.part.type.items"
	_view_name = "srm.part.type.items/o2m-list"
	_description = "Type of SRM Part Items"
