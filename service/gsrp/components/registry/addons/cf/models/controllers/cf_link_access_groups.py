from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCfLinkAccessGroups(ViewModelFindController):
	_name = "find:cf.link.access.groups"
	_view_name = "cf.link.access.groups/find"
	_description = "Link Access Groups"

class ViewModelO2MFormCfLinkAccessGroups(ViewModelO2MFormController):
	_name = "o2m-form:cf.link.access.groups"
	_view_name = "cf.link.access.groups/o2m-form"
	_description = "Link Access Groups"

class ViewModelO2MListCfLinkAccessGroups(ViewModelO2MListController):
	_name = "o2m-list:cf.link.access.groups"
	_view_name = "cf.link.access.groups/o2m-list"
	_description = "Link Access Groups"
