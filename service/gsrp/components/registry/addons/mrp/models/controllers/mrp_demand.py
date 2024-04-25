from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchMrpDemand(ViewModelSearchController):
	_name = "search:mrp.demand"
	_view_name = "mrp.demand/search"
	_description = "MRP Demand"

class ViewModelFindMrpDemand(ViewModelFindController):
	_name = "find:mrp.demand"
	_view_name = "mrp.demand/find"
	_description = "MRP Demand"

class ViewModelListMrpDemand(ViewModelListController):
	_name = "list:mrp.demand"
	_view_name = "mrp.demand/list"
	_description = "MRP Demand"

class ViewModelFormModalMrpDemand(ViewModelFormModalController):
	_name = "form.modal:mrp.demand"
	_view_name = "mrp.demand/form.modal"
	_description = "MRP Demand"

class ViewModelFormMrpDemand(ViewModelFormController):
	_name = "form:mrp.demand"
	_view_name = "mrp.demand/form"
	_description = "MRP Demand"

class ViewModelGanttMrpDemand(ViewModelGanttController):
	_name = "gantt:mrp.demand"
	_view_name = "mrp.demand/gantt"
	_description = "MRP Demand"

class ViewModelScheduleMrpDemand(ViewModelScheduleController):
	_name = "schedule:mrp.demand"
	_view_name = "mrp.demand/schedule"
	_description = "MRP Demand"

class ViewModelCalendarMrpDemand(ViewModelCalendarController):
	_name = "calendar:mrp.demand"
	_view_name = "mrp.demand/calendar"
	_description = "MRP Demand"

class ViewModelGraphMrpDemand(ViewModelGraphController):
	_name = "graph:mrp.demand"
	_view_name = "mrp.demand/graph"
	_description = "MRP Demand"

class ViewModelKanbanMrpDemand(ViewModelKanbanController):
	_name = "kanban:mrp.demand"
	_view_name = "mrp.demand/kanban"
	_description = "MRP Demand"

class ViewModelMdxMrpDemand(ViewModelMdxController):
	_name = "mdx:mrp.demand"
	_view_name = "mrp.demand/mdx"
	_description = "MRP Demand"
