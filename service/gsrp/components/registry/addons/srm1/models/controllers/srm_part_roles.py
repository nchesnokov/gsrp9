from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartRoles(ViewModelFindController):
	_name = "find:srm.part.roles"
	_view_name = "srm.part.roles/find"
	_description = "SRM Part Roles"

class ViewModelO2MFormSrmPartRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.roles"
	_view_name = "srm.part.roles/o2m-form"
	_description = "SRM Part Roles"

class ViewModelO2MListSrmPartRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.part.roles"
	_view_name = "srm.part.roles/o2m-list"
	_description = "SRM Part Roles"
