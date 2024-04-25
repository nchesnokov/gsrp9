from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfFolderAccessOthers(ViewModelFindController):
	_name = "find:cf.folder.access.others"
	_view_name = "cf.folder.access.others/find"
	_description = "Folder Access Others"

class ViewModelO2MFormCfFolderAccessOthers(ViewModelO2MFormController):
	_name = "o2m-form:cf.folder.access.others"
	_view_name = "cf.folder.access.others/o2m-form"
	_description = "Folder Access Others"

class ViewModelO2MListCfFolderAccessOthers(ViewModelO2MListController):
	_name = "o2m-list:cf.folder.access.others"
	_view_name = "cf.folder.access.others/o2m-list"
	_description = "Folder Access Others"
