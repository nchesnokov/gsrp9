from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjPortfolio(ViewModelSearchController):
	_name = "search:prj.portfolio"
	_view_name = "prj.portfolio/search"
	_description = "Projects Portfolio"

class ViewModelFindPrjPortfolio(ViewModelFindController):
	_name = "find:prj.portfolio"
	_view_name = "prj.portfolio/find"
	_description = "Projects Portfolio"

class ViewModelListPrjPortfolio(ViewModelListController):
	_name = "list:prj.portfolio"
	_view_name = "prj.portfolio/list"
	_description = "Projects Portfolio"

class ViewModelFormModalPrjPortfolio(ViewModelFormModalController):
	_name = "form.modal:prj.portfolio"
	_view_name = "prj.portfolio/form.modal"
	_description = "Projects Portfolio"

class ViewModelFormPrjPortfolio(ViewModelFormController):
	_name = "form:prj.portfolio"
	_view_name = "prj.portfolio/form"
	_description = "Projects Portfolio"

class ViewModelGanttPrjPortfolio(ViewModelGanttController):
	_name = "gantt:prj.portfolio"
	_view_name = "prj.portfolio/gantt"
	_description = "Projects Portfolio"

class ViewModelSchedulePrjPortfolio(ViewModelScheduleController):
	_name = "schedule:prj.portfolio"
	_view_name = "prj.portfolio/schedule"
	_description = "Projects Portfolio"

class ViewModelKanbanPrjPortfolio(ViewModelKanbanController):
	_name = "kanban:prj.portfolio"
	_view_name = "prj.portfolio/kanban"
	_description = "Projects Portfolio"

class ViewModelTreePrjPortfolio(ViewModelTreeController):
	_name = "tree:prj.portfolio"
	_view_name = "prj.portfolio/tree"
	_description = "Projects Portfolio"
