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

class ViewModelSearchCtrmRequests(ViewModelSearchController):
	_name = "search:ctrm.requests"
	_view_name = "ctrm.requests/search"
	_description = "CTRM Request"

class ViewModelFindCtrmRequests(ViewModelFindController):
	_name = "find:ctrm.requests"
	_view_name = "ctrm.requests/find"
	_description = "CTRM Request"

class ViewModelListCtrmRequests(ViewModelListController):
	_name = "list:ctrm.requests"
	_view_name = "ctrm.requests/list"
	_description = "CTRM Request"

class ViewModelFormModalCtrmRequests(ViewModelFormModalController):
	_name = "form.modal:ctrm.requests"
	_view_name = "ctrm.requests/form.modal"
	_description = "CTRM Request"

class ViewModelFormCtrmRequests(ViewModelFormController):
	_name = "form:ctrm.requests"
	_view_name = "ctrm.requests/form"
	_description = "CTRM Request"

class ViewModelGanttCtrmRequests(ViewModelGanttController):
	_name = "gantt:ctrm.requests"
	_view_name = "ctrm.requests/gantt"
	_description = "CTRM Request"

class ViewModelScheduleCtrmRequests(ViewModelScheduleController):
	_name = "schedule:ctrm.requests"
	_view_name = "ctrm.requests/schedule"
	_description = "CTRM Request"

class ViewModelCalendarCtrmRequests(ViewModelCalendarController):
	_name = "calendar:ctrm.requests"
	_view_name = "ctrm.requests/calendar"
	_description = "CTRM Request"

class ViewModelGraphCtrmRequests(ViewModelGraphController):
	_name = "graph:ctrm.requests"
	_view_name = "ctrm.requests/graph"
	_description = "CTRM Request"

class ViewModelKanbanCtrmRequests(ViewModelKanbanController):
	_name = "kanban:ctrm.requests"
	_view_name = "ctrm.requests/kanban"
	_description = "CTRM Request"

class ViewModelMdxCtrmRequests(ViewModelMdxController):
	_name = "mdx:ctrm.requests"
	_view_name = "ctrm.requests/mdx"
	_description = "CTRM Request"
