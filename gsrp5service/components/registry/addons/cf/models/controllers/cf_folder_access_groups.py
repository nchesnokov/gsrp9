from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfFolderAccessGroups(ViewModelFindController):
	_name = "find:cf.folder.access.groups"
	_view_name = "cf.folder.access.groups/find"
	_description = "Folder Access Groups"

class ViewModelO2MFormCfFolderAccessGroups(ViewModelO2MFormController):
	_name = "o2m-form:cf.folder.access.groups"
	_view_name = "cf.folder.access.groups/o2m-form"
	_description = "Folder Access Groups"

class ViewModelO2MListCfFolderAccessGroups(ViewModelO2MListController):
	_name = "o2m-list:cf.folder.access.groups"
	_view_name = "cf.folder.access.groups/o2m-list"
	_description = "Folder Access Groups"
