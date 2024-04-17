from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjStage(ViewModelSearchController):
	_name = "search:prj.stage"
	_view_name = "prj.stage/search"
	_description = "Project Stage"

class ViewModelFindPrjStage(ViewModelFindController):
	_name = "find:prj.stage"
	_view_name = "prj.stage/find"
	_description = "Project Stage"

class ViewModelListPrjStage(ViewModelListController):
	_name = "list:prj.stage"
	_view_name = "prj.stage/list"
	_description = "Project Stage"

class ViewModelFormModalPrjStage(ViewModelFormModalController):
	_name = "form.modal:prj.stage"
	_view_name = "prj.stage/form.modal"
	_description = "Project Stage"

class ViewModelFormPrjStage(ViewModelFormController):
	_name = "form:prj.stage"
	_view_name = "prj.stage/form"
	_description = "Project Stage"

class ViewModelGanttPrjStage(ViewModelGanttController):
	_name = "gantt:prj.stage"
	_view_name = "prj.stage/gantt"
	_description = "Project Stage"

class ViewModelSchedulePrjStage(ViewModelScheduleController):
	_name = "schedule:prj.stage"
	_view_name = "prj.stage/schedule"
	_description = "Project Stage"

class ViewModelKanbanPrjStage(ViewModelKanbanController):
	_name = "kanban:prj.stage"
	_view_name = "prj.stage/kanban"
	_description = "Project Stage"

class ViewModelTreePrjStage(ViewModelTreeController):
	_name = "tree:prj.stage"
	_view_name = "prj.stage/tree"
	_description = "Project Stage"
