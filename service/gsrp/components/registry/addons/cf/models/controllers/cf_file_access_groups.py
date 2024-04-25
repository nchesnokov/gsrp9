from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfFileAccessGroups(ViewModelFindController):
	_name = "find:cf.file.access.groups"
	_view_name = "cf.file.access.groups/find"
	_description = "File Access Groups"

class ViewModelO2MFormCfFileAccessGroups(ViewModelO2MFormController):
	_name = "o2m-form:cf.file.access.groups"
	_view_name = "cf.file.access.groups/o2m-form"
	_description = "File Access Groups"

class ViewModelO2MListCfFileAccessGroups(ViewModelO2MListController):
	_name = "o2m-list:cf.file.access.groups"
	_view_name = "cf.file.access.groups/o2m-list"
	_description = "File Access Groups"
