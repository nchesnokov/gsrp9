from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionDeadlines(ViewModelFindController):
	_name = "find:srm.decision.deadlines"
	_view_name = "srm.decision.deadlines/find"
	_description = "SRM Decision Deadlines"

class ViewModelO2MFormSrmDecisionDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.deadlines"
	_view_name = "srm.decision.deadlines/o2m-form"
	_description = "SRM Decision Deadlines"

class ViewModelO2MGanttSrmDecisionDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.decision.deadlines"
	_view_name = "srm.decision.deadlines/o2m-gantt"
	_description = "SRM Decision Deadlines"

class ViewModelO2MScheduleSrmDecisionDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.decision.deadlines"
	_view_name = "srm.decision.deadlines/o2m-schedule"
	_description = "SRM Decision Deadlines"

class ViewModelO2MListSrmDecisionDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.deadlines"
	_view_name = "srm.decision.deadlines/o2m-list"
	_description = "SRM Decision Deadlines"
