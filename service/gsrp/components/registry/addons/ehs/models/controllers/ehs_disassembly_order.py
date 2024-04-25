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

class ViewModelSearchEhsDisassemblyOrder(ViewModelSearchController):
	_name = "search:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/search"
	_description = "Disassembly Order"

class ViewModelFindEhsDisassemblyOrder(ViewModelFindController):
	_name = "find:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/find"
	_description = "Disassembly Order"

class ViewModelListEhsDisassemblyOrder(ViewModelListController):
	_name = "list:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/list"
	_description = "Disassembly Order"

class ViewModelFormModalEhsDisassemblyOrder(ViewModelFormModalController):
	_name = "form.modal:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/form.modal"
	_description = "Disassembly Order"

class ViewModelFormEhsDisassemblyOrder(ViewModelFormController):
	_name = "form:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/form"
	_description = "Disassembly Order"

class ViewModelGanttEhsDisassemblyOrder(ViewModelGanttController):
	_name = "gantt:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/gantt"
	_description = "Disassembly Order"

class ViewModelScheduleEhsDisassemblyOrder(ViewModelScheduleController):
	_name = "schedule:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/schedule"
	_description = "Disassembly Order"

class ViewModelCalendarEhsDisassemblyOrder(ViewModelCalendarController):
	_name = "calendar:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/calendar"
	_description = "Disassembly Order"

class ViewModelGraphEhsDisassemblyOrder(ViewModelGraphController):
	_name = "graph:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/graph"
	_description = "Disassembly Order"

class ViewModelKanbanEhsDisassemblyOrder(ViewModelKanbanController):
	_name = "kanban:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/kanban"
	_description = "Disassembly Order"

class ViewModelMdxEhsDisassemblyOrder(ViewModelMdxController):
	_name = "mdx:ehs.disassembly.order"
	_view_name = "ehs.disassembly.order/mdx"
	_description = "Disassembly Order"
