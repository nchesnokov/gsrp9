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

class ViewModelSearchMmDisassemblyOrders(ViewModelSearchController):
	_name = "search:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/search"
	_description = "Disassembly Order"

class ViewModelFindMmDisassemblyOrders(ViewModelFindController):
	_name = "find:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/find"
	_description = "Disassembly Order"

class ViewModelListMmDisassemblyOrders(ViewModelListController):
	_name = "list:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/list"
	_description = "Disassembly Order"

class ViewModelFormModalMmDisassemblyOrders(ViewModelFormModalController):
	_name = "form.modal:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/form.modal"
	_description = "Disassembly Order"

class ViewModelFormMmDisassemblyOrders(ViewModelFormController):
	_name = "form:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/form"
	_description = "Disassembly Order"

class ViewModelGanttMmDisassemblyOrders(ViewModelGanttController):
	_name = "gantt:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/gantt"
	_description = "Disassembly Order"

class ViewModelScheduleMmDisassemblyOrders(ViewModelScheduleController):
	_name = "schedule:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/schedule"
	_description = "Disassembly Order"

class ViewModelCalendarMmDisassemblyOrders(ViewModelCalendarController):
	_name = "calendar:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/calendar"
	_description = "Disassembly Order"

class ViewModelGraphMmDisassemblyOrders(ViewModelGraphController):
	_name = "graph:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/graph"
	_description = "Disassembly Order"

class ViewModelKanbanMmDisassemblyOrders(ViewModelKanbanController):
	_name = "kanban:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/kanban"
	_description = "Disassembly Order"

class ViewModelMdxMmDisassemblyOrders(ViewModelMdxController):
	_name = "mdx:mm.disassembly.orders"
	_view_name = "mm.disassembly.orders/mdx"
	_description = "Disassembly Order"
