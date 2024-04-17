from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionRoles(ViewModelFindController):
	_name = "find:srm.decision.roles"
	_view_name = "srm.decision.roles/find"
	_description = "SRM Decision Roles"

class ViewModelO2MFormSrmDecisionRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.roles"
	_view_name = "srm.decision.roles/o2m-form"
	_description = "SRM Decision Roles"

class ViewModelO2MListSrmDecisionRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.roles"
	_view_name = "srm.decision.roles/o2m-list"
	_description = "SRM Decision Roles"
