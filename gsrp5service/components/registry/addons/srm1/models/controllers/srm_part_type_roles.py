from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartTypeRoles(ViewModelFindController):
	_name = "find:srm.part.type.roles"
	_view_name = "srm.part.type.roles/find"
	_description = "Role SRM Part Types"

class ViewModelO2MFormSrmPartTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.type.roles"
	_view_name = "srm.part.type.roles/o2m-form"
	_description = "Role SRM Part Types"

class ViewModelO2MListSrmPartTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.part.type.roles"
	_view_name = "srm.part.type.roles/o2m-list"
	_description = "Role SRM Part Types"
