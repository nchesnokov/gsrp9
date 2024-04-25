from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseTypeItems(ViewModelFindController):
	_name = "find:srm.response.type.items"
	_view_name = "srm.response.type.items/find"
	_description = "Type of SRM Response Items"

class ViewModelO2MFormSrmResponseTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.type.items"
	_view_name = "srm.response.type.items/o2m-form"
	_description = "Type of SRM Response Items"

class ViewModelO2MListSrmResponseTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.response.type.items"
	_view_name = "srm.response.type.items/o2m-list"
	_description = "Type of SRM Response Items"
