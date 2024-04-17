from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindBcUserObjAuths(ViewModelFindController):
	_name = "find:bc.user.obj.auths"
	_view_name = "bc.user.obj.auths/find"
	_description = "User Auth Objects"

class ViewModelO2MFormBcUserObjAuths(ViewModelO2MFormController):
	_name = "o2m-form:bc.user.obj.auths"
	_view_name = "bc.user.obj.auths/o2m-form"
	_description = "User Auth Objects"

class ViewModelO2MListBcUserObjAuths(ViewModelO2MListController):
	_name = "o2m-list:bc.user.obj.auths"
	_view_name = "bc.user.obj.auths/o2m-list"
	_description = "User Auth Objects"
