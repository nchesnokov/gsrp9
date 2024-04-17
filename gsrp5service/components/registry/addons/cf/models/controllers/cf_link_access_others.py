from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfLinkAccessOthers(ViewModelFindController):
	_name = "find:cf.link.access.others"
	_view_name = "cf.link.access.others/find"
	_description = "Link Access Others"

class ViewModelO2MFormCfLinkAccessOthers(ViewModelO2MFormController):
	_name = "o2m-form:cf.link.access.others"
	_view_name = "cf.link.access.others/o2m-form"
	_description = "Link Access Others"

class ViewModelO2MListCfLinkAccessOthers(ViewModelO2MListController):
	_name = "o2m-list:cf.link.access.others"
	_view_name = "cf.link.access.others/o2m-list"
	_description = "Link Access Others"
