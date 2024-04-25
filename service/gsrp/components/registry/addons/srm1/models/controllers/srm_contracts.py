from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchSrmContracts(ViewModelSearchController):
	_name = "search:srm.contracts"
	_view_name = "srm.contracts/search"
	_description = "SRM Contract"

class ViewModelFindSrmContracts(ViewModelFindController):
	_name = "find:srm.contracts"
	_view_name = "srm.contracts/find"
	_description = "SRM Contract"

class ViewModelListSrmContracts(ViewModelListController):
	_name = "list:srm.contracts"
	_view_name = "srm.contracts/list"
	_description = "SRM Contract"

class ViewModelFormModalSrmContracts(ViewModelFormModalController):
	_name = "form.modal:srm.contracts"
	_view_name = "srm.contracts/form.modal"
	_description = "SRM Contract"

class ViewModelFormSrmContracts(ViewModelFormController):
	_name = "form:srm.contracts"
	_view_name = "srm.contracts/form"
	_description = "SRM Contract"

class ViewModelGanttSrmContracts(ViewModelGanttController):
	_name = "gantt:srm.contracts"
	_view_name = "srm.contracts/gantt"
	_description = "SRM Contract"

class ViewModelScheduleSrmContracts(ViewModelScheduleController):
	_name = "schedule:srm.contracts"
	_view_name = "srm.contracts/schedule"
	_description = "SRM Contract"

class ViewModelCalendarSrmContracts(ViewModelCalendarController):
	_name = "calendar:srm.contracts"
	_view_name = "srm.contracts/calendar"
	_description = "SRM Contract"

class ViewModelGraphSrmContracts(ViewModelGraphController):
	_name = "graph:srm.contracts"
	_view_name = "srm.contracts/graph"
	_description = "SRM Contract"

class ViewModelMdxSrmContracts(ViewModelMdxController):
	_name = "mdx:srm.contracts"
	_view_name = "srm.contracts/mdx"
	_description = "SRM Contract"
