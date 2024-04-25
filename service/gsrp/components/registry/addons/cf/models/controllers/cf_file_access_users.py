from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfFileAccessUsers(ViewModelFindController):
	_name = "find:cf.file.access.users"
	_view_name = "cf.file.access.users/find"
	_description = "File Access Users"

class ViewModelO2MFormCfFileAccessUsers(ViewModelO2MFormController):
	_name = "o2m-form:cf.file.access.users"
	_view_name = "cf.file.access.users/o2m-form"
	_description = "File Access Users"

class ViewModelO2MListCfFileAccessUsers(ViewModelO2MListController):
	_name = "o2m-list:cf.file.access.users"
	_view_name = "cf.file.access.users/o2m-list"
	_description = "File Access Users"
