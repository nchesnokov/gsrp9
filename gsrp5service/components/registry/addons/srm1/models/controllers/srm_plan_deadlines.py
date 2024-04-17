from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanDeadlines(ViewModelFindController):
	_name = "find:srm.plan.deadlines"
	_view_name = "srm.plan.deadlines/find"
	_description = "SRM Plan Deadlines"

class ViewModelO2MFormSrmPlanDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.deadlines"
	_view_name = "srm.plan.deadlines/o2m-form"
	_description = "SRM Plan Deadlines"

class ViewModelO2MGanttSrmPlanDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.plan.deadlines"
	_view_name = "srm.plan.deadlines/o2m-gantt"
	_description = "SRM Plan Deadlines"

class ViewModelO2MScheduleSrmPlanDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.plan.deadlines"
	_view_name = "srm.plan.deadlines/o2m-schedule"
	_description = "SRM Plan Deadlines"

class ViewModelO2MListSrmPlanDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.deadlines"
	_view_name = "srm.plan.deadlines/o2m-list"
	_description = "SRM Plan Deadlines"
