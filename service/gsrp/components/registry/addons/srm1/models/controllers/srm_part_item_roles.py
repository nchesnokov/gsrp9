from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartItemRoles(ViewModelFindController):
	_name = "find:srm.part.item.roles"
	_view_name = "srm.part.item.roles/find"
	_description = "SRM Part Roles"

class ViewModelO2MFormSrmPartItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.item.roles"
	_view_name = "srm.part.item.roles/o2m-form"
	_description = "SRM Part Roles"

class ViewModelO2MListSrmPartItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.part.item.roles"
	_view_name = "srm.part.item.roles/o2m-list"
	_description = "SRM Part Roles"
