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

class ViewModelSearchSrmEvolutions(ViewModelSearchController):
	_name = "search:srm.evolutions"
	_view_name = "srm.evolutions/search"
	_description = "SRM Evolution"

class ViewModelFindSrmEvolutions(ViewModelFindController):
	_name = "find:srm.evolutions"
	_view_name = "srm.evolutions/find"
	_description = "SRM Evolution"

class ViewModelListSrmEvolutions(ViewModelListController):
	_name = "list:srm.evolutions"
	_view_name = "srm.evolutions/list"
	_description = "SRM Evolution"

class ViewModelFormModalSrmEvolutions(ViewModelFormModalController):
	_name = "form.modal:srm.evolutions"
	_view_name = "srm.evolutions/form.modal"
	_description = "SRM Evolution"

class ViewModelFormSrmEvolutions(ViewModelFormController):
	_name = "form:srm.evolutions"
	_view_name = "srm.evolutions/form"
	_description = "SRM Evolution"

class ViewModelGanttSrmEvolutions(ViewModelGanttController):
	_name = "gantt:srm.evolutions"
	_view_name = "srm.evolutions/gantt"
	_description = "SRM Evolution"

class ViewModelScheduleSrmEvolutions(ViewModelScheduleController):
	_name = "schedule:srm.evolutions"
	_view_name = "srm.evolutions/schedule"
	_description = "SRM Evolution"

class ViewModelCalendarSrmEvolutions(ViewModelCalendarController):
	_name = "calendar:srm.evolutions"
	_view_name = "srm.evolutions/calendar"
	_description = "SRM Evolution"

class ViewModelGraphSrmEvolutions(ViewModelGraphController):
	_name = "graph:srm.evolutions"
	_view_name = "srm.evolutions/graph"
	_description = "SRM Evolution"

class ViewModelMdxSrmEvolutions(ViewModelMdxController):
	_name = "mdx:srm.evolutions"
	_view_name = "srm.evolutions/mdx"
	_description = "SRM Evolution"
