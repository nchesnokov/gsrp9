from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjTask(ViewModelSearchController):
	_name = "search:prj.task"
	_view_name = "prj.task/search"
	_description = "Project Task"

class ViewModelFindPrjTask(ViewModelFindController):
	_name = "find:prj.task"
	_view_name = "prj.task/find"
	_description = "Project Task"

class ViewModelListPrjTask(ViewModelListController):
	_name = "list:prj.task"
	_view_name = "prj.task/list"
	_description = "Project Task"

class ViewModelFormModalPrjTask(ViewModelFormModalController):
	_name = "form.modal:prj.task"
	_view_name = "prj.task/form.modal"
	_description = "Project Task"

class ViewModelFormPrjTask(ViewModelFormController):
	_name = "form:prj.task"
	_view_name = "prj.task/form"
	_description = "Project Task"

class ViewModelGanttPrjTask(ViewModelGanttController):
	_name = "gantt:prj.task"
	_view_name = "prj.task/gantt"
	_description = "Project Task"

class ViewModelSchedulePrjTask(ViewModelScheduleController):
	_name = "schedule:prj.task"
	_view_name = "prj.task/schedule"
	_description = "Project Task"

class ViewModelKanbanPrjTask(ViewModelKanbanController):
	_name = "kanban:prj.task"
	_view_name = "prj.task/kanban"
	_description = "Project Task"

class ViewModelTreePrjTask(ViewModelTreeController):
	_name = "tree:prj.task"
	_view_name = "prj.task/tree"
	_description = "Project Task"
