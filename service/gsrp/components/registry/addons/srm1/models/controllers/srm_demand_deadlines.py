from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandDeadlines(ViewModelFindController):
	_name = "find:srm.demand.deadlines"
	_view_name = "srm.demand.deadlines/find"
	_description = "SRM Demand Deadlines"

class ViewModelO2MFormSrmDemandDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.deadlines"
	_view_name = "srm.demand.deadlines/o2m-form"
	_description = "SRM Demand Deadlines"

class ViewModelO2MGanttSrmDemandDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.demand.deadlines"
	_view_name = "srm.demand.deadlines/o2m-gantt"
	_description = "SRM Demand Deadlines"

class ViewModelO2MScheduleSrmDemandDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.demand.deadlines"
	_view_name = "srm.demand.deadlines/o2m-schedule"
	_description = "SRM Demand Deadlines"

class ViewModelO2MListSrmDemandDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.deadlines"
	_view_name = "srm.demand.deadlines/o2m-list"
	_description = "SRM Demand Deadlines"
