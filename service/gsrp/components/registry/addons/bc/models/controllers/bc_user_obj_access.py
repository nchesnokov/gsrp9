from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcUserObjAccess(ViewModelFindController):
	_name = "find:bc.user.obj.access"
	_view_name = "bc.user.obj.access/find"
	_description = "User Access Objects"

class ViewModelO2MFormBcUserObjAccess(ViewModelO2MFormController):
	_name = "o2m-form:bc.user.obj.access"
	_view_name = "bc.user.obj.access/o2m-form"
	_description = "User Access Objects"

class ViewModelO2MListBcUserObjAccess(ViewModelO2MListController):
	_name = "o2m-list:bc.user.obj.access"
	_view_name = "bc.user.obj.access/o2m-list"
	_description = "User Access Objects"
