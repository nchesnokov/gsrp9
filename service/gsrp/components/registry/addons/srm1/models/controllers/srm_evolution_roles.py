from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionRoles(ViewModelFindController):
	_name = "find:srm.evolution.roles"
	_view_name = "srm.evolution.roles/find"
	_description = "SRM Evolution Roles"

class ViewModelO2MFormSrmEvolutionRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.roles"
	_view_name = "srm.evolution.roles/o2m-form"
	_description = "SRM Evolution Roles"

class ViewModelO2MListSrmEvolutionRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.roles"
	_view_name = "srm.evolution.roles/o2m-list"
	_description = "SRM Evolution Roles"
