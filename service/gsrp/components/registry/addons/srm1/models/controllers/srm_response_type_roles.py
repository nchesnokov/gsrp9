from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseTypeRoles(ViewModelFindController):
	_name = "find:srm.response.type.roles"
	_view_name = "srm.response.type.roles/find"
	_description = "Role SRM Response Types"

class ViewModelO2MFormSrmResponseTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.type.roles"
	_view_name = "srm.response.type.roles/o2m-form"
	_description = "Role SRM Response Types"

class ViewModelO2MListSrmResponseTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.response.type.roles"
	_view_name = "srm.response.type.roles/o2m-list"
	_description = "Role SRM Response Types"
