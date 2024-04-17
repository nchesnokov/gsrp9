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

class ViewModelSearchScmDisassemblyOrder(ViewModelSearchController):
	_name = "search:scm.disassembly.order"
	_view_name = "scm.disassembly.order/search"
	_description = "Disassembly Order"

class ViewModelFindScmDisassemblyOrder(ViewModelFindController):
	_name = "find:scm.disassembly.order"
	_view_name = "scm.disassembly.order/find"
	_description = "Disassembly Order"

class ViewModelListScmDisassemblyOrder(ViewModelListController):
	_name = "list:scm.disassembly.order"
	_view_name = "scm.disassembly.order/list"
	_description = "Disassembly Order"

class ViewModelFormModalScmDisassemblyOrder(ViewModelFormModalController):
	_name = "form.modal:scm.disassembly.order"
	_view_name = "scm.disassembly.order/form.modal"
	_description = "Disassembly Order"

class ViewModelFormScmDisassemblyOrder(ViewModelFormController):
	_name = "form:scm.disassembly.order"
	_view_name = "scm.disassembly.order/form"
	_description = "Disassembly Order"

class ViewModelGanttScmDisassemblyOrder(ViewModelGanttController):
	_name = "gantt:scm.disassembly.order"
	_view_name = "scm.disassembly.order/gantt"
	_description = "Disassembly Order"

class ViewModelScheduleScmDisassemblyOrder(ViewModelScheduleController):
	_name = "schedule:scm.disassembly.order"
	_view_name = "scm.disassembly.order/schedule"
	_description = "Disassembly Order"

class ViewModelCalendarScmDisassemblyOrder(ViewModelCalendarController):
	_name = "calendar:scm.disassembly.order"
	_view_name = "scm.disassembly.order/calendar"
	_description = "Disassembly Order"

class ViewModelGraphScmDisassemblyOrder(ViewModelGraphController):
	_name = "graph:scm.disassembly.order"
	_view_name = "scm.disassembly.order/graph"
	_description = "Disassembly Order"

class ViewModelKanbanScmDisassemblyOrder(ViewModelKanbanController):
	_name = "kanban:scm.disassembly.order"
	_view_name = "scm.disassembly.order/kanban"
	_description = "Disassembly Order"

class ViewModelMdxScmDisassemblyOrder(ViewModelMdxController):
	_name = "mdx:scm.disassembly.order"
	_view_name = "scm.disassembly.order/mdx"
	_description = "Disassembly Order"
