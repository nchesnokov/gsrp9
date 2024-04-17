from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestTypeRoles(ViewModelFindController):
	_name = "find:srm.request.type.roles"
	_view_name = "srm.request.type.roles/find"
	_description = "Role SRM Request Types"

class ViewModelO2MFormSrmRequestTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.type.roles"
	_view_name = "srm.request.type.roles/o2m-form"
	_description = "Role SRM Request Types"

class ViewModelO2MListSrmRequestTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.request.type.roles"
	_view_name = "srm.request.type.roles/o2m-list"
	_description = "Role SRM Request Types"
