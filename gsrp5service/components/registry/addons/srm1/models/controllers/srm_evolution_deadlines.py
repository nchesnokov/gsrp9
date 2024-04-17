from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionDeadlines(ViewModelFindController):
	_name = "find:srm.evolution.deadlines"
	_view_name = "srm.evolution.deadlines/find"
	_description = "SRM Evolution Deadlines"

class ViewModelO2MFormSrmEvolutionDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.deadlines"
	_view_name = "srm.evolution.deadlines/o2m-form"
	_description = "SRM Evolution Deadlines"

class ViewModelO2MGanttSrmEvolutionDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.evolution.deadlines"
	_view_name = "srm.evolution.deadlines/o2m-gantt"
	_description = "SRM Evolution Deadlines"

class ViewModelO2MScheduleSrmEvolutionDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.evolution.deadlines"
	_view_name = "srm.evolution.deadlines/o2m-schedule"
	_description = "SRM Evolution Deadlines"

class ViewModelO2MListSrmEvolutionDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.deadlines"
	_view_name = "srm.evolution.deadlines/o2m-list"
	_description = "SRM Evolution Deadlines"
