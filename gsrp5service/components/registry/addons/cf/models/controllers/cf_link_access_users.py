from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfLinkAccessUsers(ViewModelFindController):
	_name = "find:cf.link.access.users"
	_view_name = "cf.link.access.users/find"
	_description = "Link Access Users"

class ViewModelO2MFormCfLinkAccessUsers(ViewModelO2MFormController):
	_name = "o2m-form:cf.link.access.users"
	_view_name = "cf.link.access.users/o2m-form"
	_description = "Link Access Users"

class ViewModelO2MListCfLinkAccessUsers(ViewModelO2MListController):
	_name = "o2m-list:cf.link.access.users"
	_view_name = "cf.link.access.users/o2m-list"
	_description = "Link Access Users"
