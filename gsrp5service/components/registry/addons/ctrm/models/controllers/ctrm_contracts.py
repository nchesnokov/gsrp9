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

class ViewModelSearchCtrmContracts(ViewModelSearchController):
	_name = "search:ctrm.contracts"
	_view_name = "ctrm.contracts/search"
	_description = "CTRM Contract"

class ViewModelFindCtrmContracts(ViewModelFindController):
	_name = "find:ctrm.contracts"
	_view_name = "ctrm.contracts/find"
	_description = "CTRM Contract"

class ViewModelListCtrmContracts(ViewModelListController):
	_name = "list:ctrm.contracts"
	_view_name = "ctrm.contracts/list"
	_description = "CTRM Contract"

class ViewModelFormModalCtrmContracts(ViewModelFormModalController):
	_name = "form.modal:ctrm.contracts"
	_view_name = "ctrm.contracts/form.modal"
	_description = "CTRM Contract"

class ViewModelFormCtrmContracts(ViewModelFormController):
	_name = "form:ctrm.contracts"
	_view_name = "ctrm.contracts/form"
	_description = "CTRM Contract"

class ViewModelGanttCtrmContracts(ViewModelGanttController):
	_name = "gantt:ctrm.contracts"
	_view_name = "ctrm.contracts/gantt"
	_description = "CTRM Contract"

class ViewModelScheduleCtrmContracts(ViewModelScheduleController):
	_name = "schedule:ctrm.contracts"
	_view_name = "ctrm.contracts/schedule"
	_description = "CTRM Contract"

class ViewModelCalendarCtrmContracts(ViewModelCalendarController):
	_name = "calendar:ctrm.contracts"
	_view_name = "ctrm.contracts/calendar"
	_description = "CTRM Contract"

class ViewModelGraphCtrmContracts(ViewModelGraphController):
	_name = "graph:ctrm.contracts"
	_view_name = "ctrm.contracts/graph"
	_description = "CTRM Contract"

class ViewModelKanbanCtrmContracts(ViewModelKanbanController):
	_name = "kanban:ctrm.contracts"
	_view_name = "ctrm.contracts/kanban"
	_description = "CTRM Contract"

class ViewModelMdxCtrmContracts(ViewModelMdxController):
	_name = "mdx:ctrm.contracts"
	_view_name = "ctrm.contracts/mdx"
	_description = "CTRM Contract"
