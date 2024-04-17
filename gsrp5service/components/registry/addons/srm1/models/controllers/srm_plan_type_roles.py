from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanTypeRoles(ViewModelFindController):
	_name = "find:srm.plan.type.roles"
	_view_name = "srm.plan.type.roles/find"
	_description = "Role SRM Plan Types"

class ViewModelO2MFormSrmPlanTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.type.roles"
	_view_name = "srm.plan.type.roles/o2m-form"
	_description = "Role SRM Plan Types"

class ViewModelO2MListSrmPlanTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.type.roles"
	_view_name = "srm.plan.type.roles/o2m-list"
	_description = "Role SRM Plan Types"
