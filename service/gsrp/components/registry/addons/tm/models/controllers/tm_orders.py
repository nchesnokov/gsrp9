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

class ViewModelSearchTmOrders(ViewModelSearchController):
	_name = "search:tm.orders"
	_view_name = "tm.orders/search"
	_description = "Order"

class ViewModelFindTmOrders(ViewModelFindController):
	_name = "find:tm.orders"
	_view_name = "tm.orders/find"
	_description = "Order"

class ViewModelListTmOrders(ViewModelListController):
	_name = "list:tm.orders"
	_view_name = "tm.orders/list"
	_description = "Order"

class ViewModelFormModalTmOrders(ViewModelFormModalController):
	_name = "form.modal:tm.orders"
	_view_name = "tm.orders/form.modal"
	_description = "Order"

class ViewModelFormTmOrders(ViewModelFormController):
	_name = "form:tm.orders"
	_view_name = "tm.orders/form"
	_description = "Order"

class ViewModelGanttTmOrders(ViewModelGanttController):
	_name = "gantt:tm.orders"
	_view_name = "tm.orders/gantt"
	_description = "Order"

class ViewModelScheduleTmOrders(ViewModelScheduleController):
	_name = "schedule:tm.orders"
	_view_name = "tm.orders/schedule"
	_description = "Order"

class ViewModelCalendarTmOrders(ViewModelCalendarController):
	_name = "calendar:tm.orders"
	_view_name = "tm.orders/calendar"
	_description = "Order"

class ViewModelGraphTmOrders(ViewModelGraphController):
	_name = "graph:tm.orders"
	_view_name = "tm.orders/graph"
	_description = "Order"

class ViewModelKanbanTmOrders(ViewModelKanbanController):
	_name = "kanban:tm.orders"
	_view_name = "tm.orders/kanban"
	_description = "Order"

class ViewModelMdxTmOrders(ViewModelMdxController):
	_name = "mdx:tm.orders"
	_view_name = "tm.orders/mdx"
	_description = "Order"
