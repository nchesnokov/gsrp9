from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanItemRoles(ViewModelFindController):
	_name = "find:srm.plan.item.roles"
	_view_name = "srm.plan.item.roles/find"
	_description = "SRM Plan Roles"

class ViewModelO2MFormSrmPlanItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.item.roles"
	_view_name = "srm.plan.item.roles/o2m-form"
	_description = "SRM Plan Roles"

class ViewModelO2MListSrmPlanItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.item.roles"
	_view_name = "srm.plan.item.roles/o2m-list"
	_description = "SRM Plan Roles"
