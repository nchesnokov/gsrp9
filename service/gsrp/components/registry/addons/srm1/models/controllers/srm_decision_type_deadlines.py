from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionTypeDeadlines(ViewModelFindController):
	_name = "find:srm.decision.type.deadlines"
	_view_name = "srm.decision.type.deadlines/find"
	_description = "Deadlines SRM Decision Types"

class ViewModelO2MFormSrmDecisionTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.type.deadlines"
	_view_name = "srm.decision.type.deadlines/o2m-form"
	_description = "Deadlines SRM Decision Types"

class ViewModelO2MListSrmDecisionTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.type.deadlines"
	_view_name = "srm.decision.type.deadlines/o2m-list"
	_description = "Deadlines SRM Decision Types"
