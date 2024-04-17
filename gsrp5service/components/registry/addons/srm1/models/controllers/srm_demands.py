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

class ViewModelSearchSrmDemands(ViewModelSearchController):
	_name = "search:srm.demands"
	_view_name = "srm.demands/search"
	_description = "SRM Demand"

class ViewModelFindSrmDemands(ViewModelFindController):
	_name = "find:srm.demands"
	_view_name = "srm.demands/find"
	_description = "SRM Demand"

class ViewModelListSrmDemands(ViewModelListController):
	_name = "list:srm.demands"
	_view_name = "srm.demands/list"
	_description = "SRM Demand"

class ViewModelFormModalSrmDemands(ViewModelFormModalController):
	_name = "form.modal:srm.demands"
	_view_name = "srm.demands/form.modal"
	_description = "SRM Demand"

class ViewModelFormSrmDemands(ViewModelFormController):
	_name = "form:srm.demands"
	_view_name = "srm.demands/form"
	_description = "SRM Demand"

class ViewModelGanttSrmDemands(ViewModelGanttController):
	_name = "gantt:srm.demands"
	_view_name = "srm.demands/gantt"
	_description = "SRM Demand"

class ViewModelScheduleSrmDemands(ViewModelScheduleController):
	_name = "schedule:srm.demands"
	_view_name = "srm.demands/schedule"
	_description = "SRM Demand"

class ViewModelCalendarSrmDemands(ViewModelCalendarController):
	_name = "calendar:srm.demands"
	_view_name = "srm.demands/calendar"
	_description = "SRM Demand"

class ViewModelGraphSrmDemands(ViewModelGraphController):
	_name = "graph:srm.demands"
	_view_name = "srm.demands/graph"
	_description = "SRM Demand"

class ViewModelMdxSrmDemands(ViewModelMdxController):
	_name = "mdx:srm.demands"
	_view_name = "srm.demands/mdx"
	_description = "SRM Demand"
