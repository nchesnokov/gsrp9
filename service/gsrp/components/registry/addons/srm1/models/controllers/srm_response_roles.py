from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseRoles(ViewModelFindController):
	_name = "find:srm.response.roles"
	_view_name = "srm.response.roles/find"
	_description = "SRM Response Roles"

class ViewModelO2MFormSrmResponseRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.roles"
	_view_name = "srm.response.roles/o2m-form"
	_description = "SRM Response Roles"

class ViewModelO2MListSrmResponseRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.response.roles"
	_view_name = "srm.response.roles/o2m-list"
	_description = "SRM Response Roles"
