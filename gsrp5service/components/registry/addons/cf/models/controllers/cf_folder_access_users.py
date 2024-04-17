from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfFolderAccessUsers(ViewModelFindController):
	_name = "find:cf.folder.access.users"
	_view_name = "cf.folder.access.users/find"
	_description = "File Access Users"

class ViewModelO2MFormCfFolderAccessUsers(ViewModelO2MFormController):
	_name = "o2m-form:cf.folder.access.users"
	_view_name = "cf.folder.access.users/o2m-form"
	_description = "File Access Users"

class ViewModelO2MListCfFolderAccessUsers(ViewModelO2MListController):
	_name = "o2m-list:cf.folder.access.users"
	_view_name = "cf.folder.access.users/o2m-list"
	_description = "File Access Users"
