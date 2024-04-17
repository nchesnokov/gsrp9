from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestRoles(ViewModelFindController):
	_name = "find:mrp.request.roles"
	_view_name = "mrp.request.roles/find"
	_description = "Purchase Invoice Roles"

class ViewModelO2MFormMrpRequestRoles(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.roles"
	_view_name = "mrp.request.roles/o2m-form"
	_description = "Purchase Invoice Roles"

class ViewModelO2MListMrpRequestRoles(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.roles"
	_view_name = "mrp.request.roles/o2m-list"
	_description = "Purchase Invoice Roles"
