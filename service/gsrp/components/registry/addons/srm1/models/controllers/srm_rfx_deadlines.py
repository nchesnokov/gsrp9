from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxDeadlines(ViewModelFindController):
	_name = "find:srm.rfx.deadlines"
	_view_name = "srm.rfx.deadlines/find"
	_description = "SRM RFX Deadlines"

class ViewModelO2MFormSrmRfxDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.deadlines"
	_view_name = "srm.rfx.deadlines/o2m-form"
	_description = "SRM RFX Deadlines"

class ViewModelO2MGanttSrmRfxDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.rfx.deadlines"
	_view_name = "srm.rfx.deadlines/o2m-gantt"
	_description = "SRM RFX Deadlines"

class ViewModelO2MScheduleSrmRfxDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.rfx.deadlines"
	_view_name = "srm.rfx.deadlines/o2m-schedule"
	_description = "SRM RFX Deadlines"

class ViewModelO2MListSrmRfxDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.deadlines"
	_view_name = "srm.rfx.deadlines/o2m-list"
	_description = "SRM RFX Deadlines"
