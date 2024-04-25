from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmRequestItemRoles(ViewModelFindController):
	_name = "find:ctrm.request.item.roles"
	_view_name = "ctrm.request.item.roles/find"
	_description = "CTRM Offer Item Roles"

class ViewModelO2MFormCtrmRequestItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.request.item.roles"
	_view_name = "ctrm.request.item.roles/o2m-form"
	_description = "CTRM Offer Item Roles"

class ViewModelO2MListCtrmRequestItemRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.request.item.roles"
	_view_name = "ctrm.request.item.roles/o2m-list"
	_description = "CTRM Offer Item Roles"
