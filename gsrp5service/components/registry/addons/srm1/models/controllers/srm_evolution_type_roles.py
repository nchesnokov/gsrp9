from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionTypeRoles(ViewModelFindController):
	_name = "find:srm.evolution.type.roles"
	_view_name = "srm.evolution.type.roles/find"
	_description = "Role SRM Evolution Types"

class ViewModelO2MFormSrmEvolutionTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.type.roles"
	_view_name = "srm.evolution.type.roles/o2m-form"
	_description = "Role SRM Evolution Types"

class ViewModelO2MListSrmEvolutionTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.type.roles"
	_view_name = "srm.evolution.type.roles/o2m-list"
	_description = "Role SRM Evolution Types"
