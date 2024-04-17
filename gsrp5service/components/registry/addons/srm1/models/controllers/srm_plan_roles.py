from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanRoles(ViewModelFindController):
	_name = "find:srm.plan.roles"
	_view_name = "srm.plan.roles/find"
	_description = "SRM Plan Roles"

class ViewModelO2MFormSrmPlanRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.roles"
	_view_name = "srm.plan.roles/o2m-form"
	_description = "SRM Plan Roles"

class ViewModelO2MListSrmPlanRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.roles"
	_view_name = "srm.plan.roles/o2m-list"
	_description = "SRM Plan Roles"
