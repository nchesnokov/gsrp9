from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmRequestRoles(ViewModelFindController):
	_name = "find:ctrm.request.roles"
	_view_name = "ctrm.request.roles/find"
	_description = "CTRM Request Roles"

class ViewModelO2MFormCtrmRequestRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.request.roles"
	_view_name = "ctrm.request.roles/o2m-form"
	_description = "CTRM Request Roles"

class ViewModelO2MListCtrmRequestRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.request.roles"
	_view_name = "ctrm.request.roles/o2m-list"
	_description = "CTRM Request Roles"
