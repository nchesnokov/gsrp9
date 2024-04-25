from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestItemRoles(ViewModelFindController):
	_name = "find:mrp.request.item.roles"
	_view_name = "mrp.request.item.roles/find"
	_description = "MRP Request Item Roles"

class ViewModelO2MFormMrpRequestItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.item.roles"
	_view_name = "mrp.request.item.roles/o2m-form"
	_description = "MRP Request Item Roles"

class ViewModelO2MListMrpRequestItemRoles(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.item.roles"
	_view_name = "mrp.request.item.roles/o2m-list"
	_description = "MRP Request Item Roles"
