from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionItemRoles(ViewModelFindController):
	_name = "find:srm.evolution.item.roles"
	_view_name = "srm.evolution.item.roles/find"
	_description = "SRM Evolution Roles"

class ViewModelO2MFormSrmEvolutionItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.item.roles"
	_view_name = "srm.evolution.item.roles/o2m-form"
	_description = "SRM Evolution Roles"

class ViewModelO2MListSrmEvolutionItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.item.roles"
	_view_name = "srm.evolution.item.roles/o2m-list"
	_description = "SRM Evolution Roles"
