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

class ViewModelSearchMmProductionOrders(ViewModelSearchController):
	_name = "search:mm.production.orders"
	_view_name = "mm.production.orders/search"
	_description = "Production Order"

class ViewModelFindMmProductionOrders(ViewModelFindController):
	_name = "find:mm.production.orders"
	_view_name = "mm.production.orders/find"
	_description = "Production Order"

class ViewModelListMmProductionOrders(ViewModelListController):
	_name = "list:mm.production.orders"
	_view_name = "mm.production.orders/list"
	_description = "Production Order"

class ViewModelFormModalMmProductionOrders(ViewModelFormModalController):
	_name = "form.modal:mm.production.orders"
	_view_name = "mm.production.orders/form.modal"
	_description = "Production Order"

class ViewModelFormMmProductionOrders(ViewModelFormController):
	_name = "form:mm.production.orders"
	_view_name = "mm.production.orders/form"
	_description = "Production Order"

class ViewModelGanttMmProductionOrders(ViewModelGanttController):
	_name = "gantt:mm.production.orders"
	_view_name = "mm.production.orders/gantt"
	_description = "Production Order"

class ViewModelScheduleMmProductionOrders(ViewModelScheduleController):
	_name = "schedule:mm.production.orders"
	_view_name = "mm.production.orders/schedule"
	_description = "Production Order"

class ViewModelCalendarMmProductionOrders(ViewModelCalendarController):
	_name = "calendar:mm.production.orders"
	_view_name = "mm.production.orders/calendar"
	_description = "Production Order"

class ViewModelGraphMmProductionOrders(ViewModelGraphController):
	_name = "graph:mm.production.orders"
	_view_name = "mm.production.orders/graph"
	_description = "Production Order"

class ViewModelKanbanMmProductionOrders(ViewModelKanbanController):
	_name = "kanban:mm.production.orders"
	_view_name = "mm.production.orders/kanban"
	_description = "Production Order"

class ViewModelMdxMmProductionOrders(ViewModelMdxController):
	_name = "mdx:mm.production.orders"
	_view_name = "mm.production.orders/mdx"
	_description = "Production Order"
