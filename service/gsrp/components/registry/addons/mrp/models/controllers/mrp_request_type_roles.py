from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestTypeRoles(ViewModelFindController):
	_name = "find:mrp.request.type.roles"
	_view_name = "mrp.request.type.roles/find"
	_description = "Role MRP Request Types"

class ViewModelO2MFormMrpRequestTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.type.roles"
	_view_name = "mrp.request.type.roles/o2m-form"
	_description = "Role MRP Request Types"

class ViewModelO2MListMrpRequestTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.type.roles"
	_view_name = "mrp.request.type.roles/o2m-list"
	_description = "Role MRP Request Types"
