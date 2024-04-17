from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchPrjBill(ViewModelSearchController):
	_name = "search:prj.bill"
	_view_name = "prj.bill/search"
	_description = "Projects Bill"

class ViewModelFindPrjBill(ViewModelFindController):
	_name = "find:prj.bill"
	_view_name = "prj.bill/find"
	_description = "Projects Bill"

class ViewModelListPrjBill(ViewModelListController):
	_name = "list:prj.bill"
	_view_name = "prj.bill/list"
	_description = "Projects Bill"

class ViewModelFormModalPrjBill(ViewModelFormModalController):
	_name = "form.modal:prj.bill"
	_view_name = "prj.bill/form.modal"
	_description = "Projects Bill"

class ViewModelFormPrjBill(ViewModelFormController):
	_name = "form:prj.bill"
	_view_name = "prj.bill/form"
	_description = "Projects Bill"

class ViewModelGanttPrjBill(ViewModelGanttController):
	_name = "gantt:prj.bill"
	_view_name = "prj.bill/gantt"
	_description = "Projects Bill"

class ViewModelSchedulePrjBill(ViewModelScheduleController):
	_name = "schedule:prj.bill"
	_view_name = "prj.bill/schedule"
	_description = "Projects Bill"

class ViewModelKanbanPrjBill(ViewModelKanbanController):
	_name = "kanban:prj.bill"
	_view_name = "prj.bill/kanban"
	_description = "Projects Bill"

class ViewModelTreePrjBill(ViewModelTreeController):
	_name = "tree:prj.bill"
	_view_name = "prj.bill/tree"
	_description = "Projects Bill"
