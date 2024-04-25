from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartDeadlines(ViewModelFindController):
	_name = "find:srm.part.deadlines"
	_view_name = "srm.part.deadlines/find"
	_description = "SRM Part Deadlines"

class ViewModelO2MFormSrmPartDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.deadlines"
	_view_name = "srm.part.deadlines/o2m-form"
	_description = "SRM Part Deadlines"

class ViewModelO2MGanttSrmPartDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.part.deadlines"
	_view_name = "srm.part.deadlines/o2m-gantt"
	_description = "SRM Part Deadlines"

class ViewModelO2MScheduleSrmPartDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.part.deadlines"
	_view_name = "srm.part.deadlines/o2m-schedule"
	_description = "SRM Part Deadlines"

class ViewModelO2MListSrmPartDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.part.deadlines"
	_view_name = "srm.part.deadlines/o2m-list"
	_description = "SRM Part Deadlines"
