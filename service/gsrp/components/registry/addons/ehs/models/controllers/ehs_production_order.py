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

class ViewModelSearchEhsProductionOrder(ViewModelSearchController):
	_name = "search:ehs.production.order"
	_view_name = "ehs.production.order/search"
	_description = "Production Order"

class ViewModelFindEhsProductionOrder(ViewModelFindController):
	_name = "find:ehs.production.order"
	_view_name = "ehs.production.order/find"
	_description = "Production Order"

class ViewModelListEhsProductionOrder(ViewModelListController):
	_name = "list:ehs.production.order"
	_view_name = "ehs.production.order/list"
	_description = "Production Order"

class ViewModelFormModalEhsProductionOrder(ViewModelFormModalController):
	_name = "form.modal:ehs.production.order"
	_view_name = "ehs.production.order/form.modal"
	_description = "Production Order"

class ViewModelFormEhsProductionOrder(ViewModelFormController):
	_name = "form:ehs.production.order"
	_view_name = "ehs.production.order/form"
	_description = "Production Order"

class ViewModelGanttEhsProductionOrder(ViewModelGanttController):
	_name = "gantt:ehs.production.order"
	_view_name = "ehs.production.order/gantt"
	_description = "Production Order"

class ViewModelScheduleEhsProductionOrder(ViewModelScheduleController):
	_name = "schedule:ehs.production.order"
	_view_name = "ehs.production.order/schedule"
	_description = "Production Order"

class ViewModelCalendarEhsProductionOrder(ViewModelCalendarController):
	_name = "calendar:ehs.production.order"
	_view_name = "ehs.production.order/calendar"
	_description = "Production Order"

class ViewModelGraphEhsProductionOrder(ViewModelGraphController):
	_name = "graph:ehs.production.order"
	_view_name = "ehs.production.order/graph"
	_description = "Production Order"

class ViewModelKanbanEhsProductionOrder(ViewModelKanbanController):
	_name = "kanban:ehs.production.order"
	_view_name = "ehs.production.order/kanban"
	_description = "Production Order"

class ViewModelMdxEhsProductionOrder(ViewModelMdxController):
	_name = "mdx:ehs.production.order"
	_view_name = "ehs.production.order/mdx"
	_description = "Production Order"
