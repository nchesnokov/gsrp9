from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractDeadlines(ViewModelFindController):
	_name = "find:srm.contract.deadlines"
	_view_name = "srm.contract.deadlines/find"
	_description = "SRM Contract Deadlines"

class ViewModelO2MFormSrmContractDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.deadlines"
	_view_name = "srm.contract.deadlines/o2m-form"
	_description = "SRM Contract Deadlines"

class ViewModelO2MGanttSrmContractDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.contract.deadlines"
	_view_name = "srm.contract.deadlines/o2m-gantt"
	_description = "SRM Contract Deadlines"

class ViewModelO2MScheduleSrmContractDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.contract.deadlines"
	_view_name = "srm.contract.deadlines/o2m-schedule"
	_description = "SRM Contract Deadlines"

class ViewModelO2MListSrmContractDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.deadlines"
	_view_name = "srm.contract.deadlines/o2m-list"
	_description = "SRM Contract Deadlines"
