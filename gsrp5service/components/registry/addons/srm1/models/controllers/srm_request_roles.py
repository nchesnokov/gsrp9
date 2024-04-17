from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestRoles(ViewModelFindController):
	_name = "find:srm.request.roles"
	_view_name = "srm.request.roles/find"
	_description = "SRM Request Roles"

class ViewModelO2MFormSrmRequestRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.roles"
	_view_name = "srm.request.roles/o2m-form"
	_description = "SRM Request Roles"

class ViewModelO2MListSrmRequestRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.request.roles"
	_view_name = "srm.request.roles/o2m-list"
	_description = "SRM Request Roles"
