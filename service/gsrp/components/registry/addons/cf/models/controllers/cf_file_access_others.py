from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfFileAccessOthers(ViewModelFindController):
	_name = "find:cf.file.access.others"
	_view_name = "cf.file.access.others/find"
	_description = "File Access Others"

class ViewModelO2MFormCfFileAccessOthers(ViewModelO2MFormController):
	_name = "o2m-form:cf.file.access.others"
	_view_name = "cf.file.access.others/o2m-form"
	_description = "File Access Others"

class ViewModelO2MListCfFileAccessOthers(ViewModelO2MListController):
	_name = "o2m-list:cf.file.access.others"
	_view_name = "cf.file.access.others/o2m-list"
	_description = "File Access Others"
