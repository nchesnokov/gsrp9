from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestDeadlines(ViewModelFindController):
	_name = "find:srm.request.deadlines"
	_view_name = "srm.request.deadlines/find"
	_description = "SRM Request Deadlines"

class ViewModelO2MFormSrmRequestDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.deadlines"
	_view_name = "srm.request.deadlines/o2m-form"
	_description = "SRM Request Deadlines"

class ViewModelO2MGanttSrmRequestDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.request.deadlines"
	_view_name = "srm.request.deadlines/o2m-gantt"
	_description = "SRM Request Deadlines"

class ViewModelO2MScheduleSrmRequestDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.request.deadlines"
	_view_name = "srm.request.deadlines/o2m-schedule"
	_description = "SRM Request Deadlines"

class ViewModelO2MListSrmRequestDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.request.deadlines"
	_view_name = "srm.request.deadlines/o2m-list"
	_description = "SRM Request Deadlines"
