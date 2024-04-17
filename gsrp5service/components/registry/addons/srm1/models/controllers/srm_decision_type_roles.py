from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionTypeRoles(ViewModelFindController):
	_name = "find:srm.decision.type.roles"
	_view_name = "srm.decision.type.roles/find"
	_description = "Role SRM Decision Types"

class ViewModelO2MFormSrmDecisionTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.type.roles"
	_view_name = "srm.decision.type.roles/o2m-form"
	_description = "Role SRM Decision Types"

class ViewModelO2MListSrmDecisionTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.type.roles"
	_view_name = "srm.decision.type.roles/o2m-list"
	_description = "Role SRM Decision Types"
