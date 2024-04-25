from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmRequestTypeRoles(ViewModelFindController):
	_name = "find:ctrm.request.type.roles"
	_view_name = "ctrm.request.type.roles/find"
	_description = "Role CTRM Request Types"

class ViewModelO2MFormCtrmRequestTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.request.type.roles"
	_view_name = "ctrm.request.type.roles/o2m-form"
	_description = "Role CTRM Request Types"

class ViewModelO2MListCtrmRequestTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.request.type.roles"
	_view_name = "ctrm.request.type.roles/o2m-list"
	_description = "Role CTRM Request Types"
