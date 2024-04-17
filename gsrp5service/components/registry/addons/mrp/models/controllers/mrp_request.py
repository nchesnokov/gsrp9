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

class ViewModelSearchMrpRequest(ViewModelSearchController):
	_name = "search:mrp.request"
	_view_name = "mrp.request/search"
	_description = "MRP Request"

class ViewModelFindMrpRequest(ViewModelFindController):
	_name = "find:mrp.request"
	_view_name = "mrp.request/find"
	_description = "MRP Request"

class ViewModelListMrpRequest(ViewModelListController):
	_name = "list:mrp.request"
	_view_name = "mrp.request/list"
	_description = "MRP Request"

class ViewModelFormModalMrpRequest(ViewModelFormModalController):
	_name = "form.modal:mrp.request"
	_view_name = "mrp.request/form.modal"
	_description = "MRP Request"

class ViewModelFormMrpRequest(ViewModelFormController):
	_name = "form:mrp.request"
	_view_name = "mrp.request/form"
	_description = "MRP Request"

class ViewModelGanttMrpRequest(ViewModelGanttController):
	_name = "gantt:mrp.request"
	_view_name = "mrp.request/gantt"
	_description = "MRP Request"

class ViewModelScheduleMrpRequest(ViewModelScheduleController):
	_name = "schedule:mrp.request"
	_view_name = "mrp.request/schedule"
	_description = "MRP Request"

class ViewModelCalendarMrpRequest(ViewModelCalendarController):
	_name = "calendar:mrp.request"
	_view_name = "mrp.request/calendar"
	_description = "MRP Request"

class ViewModelGraphMrpRequest(ViewModelGraphController):
	_name = "graph:mrp.request"
	_view_name = "mrp.request/graph"
	_description = "MRP Request"

class ViewModelKanbanMrpRequest(ViewModelKanbanController):
	_name = "kanban:mrp.request"
	_view_name = "mrp.request/kanban"
	_description = "MRP Request"

class ViewModelMdxMrpRequest(ViewModelMdxController):
	_name = "mdx:mrp.request"
	_view_name = "mrp.request/mdx"
	_description = "MRP Request"
