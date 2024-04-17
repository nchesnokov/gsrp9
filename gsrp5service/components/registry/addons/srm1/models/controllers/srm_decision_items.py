from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionItems(ViewModelFindController):
	_name = "find:srm.decision.items"
	_view_name = "srm.decision.items/find"
	_description = "SRM Decision Item"

class ViewModelO2MFormSrmDecisionItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.items"
	_view_name = "srm.decision.items/o2m-form"
	_description = "SRM Decision Item"

class ViewModelO2MListSrmDecisionItems(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.items"
	_view_name = "srm.decision.items/o2m-list"
	_description = "SRM Decision Item"
