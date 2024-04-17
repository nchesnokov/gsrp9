from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseItemRoles(ViewModelFindController):
	_name = "find:srm.response.item.roles"
	_view_name = "srm.response.item.roles/find"
	_description = "SRM Response Roles"

class ViewModelO2MFormSrmResponseItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.item.roles"
	_view_name = "srm.response.item.roles/o2m-form"
	_description = "SRM Response Roles"

class ViewModelO2MListSrmResponseItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.response.item.roles"
	_view_name = "srm.response.item.roles/o2m-list"
	_description = "SRM Response Roles"
