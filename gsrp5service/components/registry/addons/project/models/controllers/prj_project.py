from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjProject(ViewModelSearchController):
	_name = "search:prj.project"
	_view_name = "prj.project/search"
	_description = "Project"

class ViewModelFindPrjProject(ViewModelFindController):
	_name = "find:prj.project"
	_view_name = "prj.project/find"
	_description = "Project"

class ViewModelListPrjProject(ViewModelListController):
	_name = "list:prj.project"
	_view_name = "prj.project/list"
	_description = "Project"

class ViewModelFormModalPrjProject(ViewModelFormModalController):
	_name = "form.modal:prj.project"
	_view_name = "prj.project/form.modal"
	_description = "Project"

class ViewModelFormPrjProject(ViewModelFormController):
	_name = "form:prj.project"
	_view_name = "prj.project/form"
	_description = "Project"

class ViewModelGanttPrjProject(ViewModelGanttController):
	_name = "gantt:prj.project"
	_view_name = "prj.project/gantt"
	_description = "Project"

class ViewModelSchedulePrjProject(ViewModelScheduleController):
	_name = "schedule:prj.project"
	_view_name = "prj.project/schedule"
	_description = "Project"

class ViewModelKanbanPrjProject(ViewModelKanbanController):
	_name = "kanban:prj.project"
	_view_name = "prj.project/kanban"
	_description = "Project"

class ViewModelTreePrjProject(ViewModelTreeController):
	_name = "tree:prj.project"
	_view_name = "prj.project/tree"
	_description = "Project"
