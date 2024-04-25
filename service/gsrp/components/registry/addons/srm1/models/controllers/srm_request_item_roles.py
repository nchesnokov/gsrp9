from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestItemRoles(ViewModelFindController):
	_name = "find:srm.request.item.roles"
	_view_name = "srm.request.item.roles/find"
	_description = "SRM Request Roles"

class ViewModelO2MFormSrmRequestItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.item.roles"
	_view_name = "srm.request.item.roles/o2m-form"
	_description = "SRM Request Roles"

class ViewModelO2MListSrmRequestItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.request.item.roles"
	_view_name = "srm.request.item.roles/o2m-list"
	_description = "SRM Request Roles"
