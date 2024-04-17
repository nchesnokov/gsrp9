from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseDeadlines(ViewModelFindController):
	_name = "find:srm.response.deadlines"
	_view_name = "srm.response.deadlines/find"
	_description = "SRM Response Deadlines"

class ViewModelO2MFormSrmResponseDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.deadlines"
	_view_name = "srm.response.deadlines/o2m-form"
	_description = "SRM Response Deadlines"

class ViewModelO2MGanttSrmResponseDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.response.deadlines"
	_view_name = "srm.response.deadlines/o2m-gantt"
	_description = "SRM Response Deadlines"

class ViewModelO2MScheduleSrmResponseDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.response.deadlines"
	_view_name = "srm.response.deadlines/o2m-schedule"
	_description = "SRM Response Deadlines"

class ViewModelO2MListSrmResponseDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.response.deadlines"
	_view_name = "srm.response.deadlines/o2m-list"
	_description = "SRM Response Deadlines"
