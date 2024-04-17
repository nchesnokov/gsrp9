from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionItemRoles(ViewModelFindController):
	_name = "find:srm.decision.item.roles"
	_view_name = "srm.decision.item.roles/find"
	_description = "SRM Decision Roles"

class ViewModelO2MFormSrmDecisionItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.item.roles"
	_view_name = "srm.decision.item.roles/o2m-form"
	_description = "SRM Decision Roles"

class ViewModelO2MListSrmDecisionItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.item.roles"
	_view_name = "srm.decision.item.roles/o2m-list"
	_description = "SRM Decision Roles"
