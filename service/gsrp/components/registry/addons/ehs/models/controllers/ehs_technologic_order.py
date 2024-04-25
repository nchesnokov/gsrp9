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

class ViewModelSearchEhsTechnologicOrder(ViewModelSearchController):
	_name = "search:ehs.technologic.order"
	_view_name = "ehs.technologic.order/search"
	_description = "Technologic Order"

class ViewModelFindEhsTechnologicOrder(ViewModelFindController):
	_name = "find:ehs.technologic.order"
	_view_name = "ehs.technologic.order/find"
	_description = "Technologic Order"

class ViewModelListEhsTechnologicOrder(ViewModelListController):
	_name = "list:ehs.technologic.order"
	_view_name = "ehs.technologic.order/list"
	_description = "Technologic Order"

class ViewModelFormModalEhsTechnologicOrder(ViewModelFormModalController):
	_name = "form.modal:ehs.technologic.order"
	_view_name = "ehs.technologic.order/form.modal"
	_description = "Technologic Order"

class ViewModelFormEhsTechnologicOrder(ViewModelFormController):
	_name = "form:ehs.technologic.order"
	_view_name = "ehs.technologic.order/form"
	_description = "Technologic Order"

class ViewModelGanttEhsTechnologicOrder(ViewModelGanttController):
	_name = "gantt:ehs.technologic.order"
	_view_name = "ehs.technologic.order/gantt"
	_description = "Technologic Order"

class ViewModelScheduleEhsTechnologicOrder(ViewModelScheduleController):
	_name = "schedule:ehs.technologic.order"
	_view_name = "ehs.technologic.order/schedule"
	_description = "Technologic Order"

class ViewModelCalendarEhsTechnologicOrder(ViewModelCalendarController):
	_name = "calendar:ehs.technologic.order"
	_view_name = "ehs.technologic.order/calendar"
	_description = "Technologic Order"

class ViewModelGraphEhsTechnologicOrder(ViewModelGraphController):
	_name = "graph:ehs.technologic.order"
	_view_name = "ehs.technologic.order/graph"
	_description = "Technologic Order"

class ViewModelKanbanEhsTechnologicOrder(ViewModelKanbanController):
	_name = "kanban:ehs.technologic.order"
	_view_name = "ehs.technologic.order/kanban"
	_description = "Technologic Order"

class ViewModelMdxEhsTechnologicOrder(ViewModelMdxController):
	_name = "mdx:ehs.technologic.order"
	_view_name = "ehs.technologic.order/mdx"
	_description = "Technologic Order"
