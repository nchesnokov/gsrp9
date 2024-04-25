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

class ViewModelSearchMmTechnologicOrders(ViewModelSearchController):
	_name = "search:mm.technologic.orders"
	_view_name = "mm.technologic.orders/search"
	_description = "Technologic Order"

class ViewModelFindMmTechnologicOrders(ViewModelFindController):
	_name = "find:mm.technologic.orders"
	_view_name = "mm.technologic.orders/find"
	_description = "Technologic Order"

class ViewModelListMmTechnologicOrders(ViewModelListController):
	_name = "list:mm.technologic.orders"
	_view_name = "mm.technologic.orders/list"
	_description = "Technologic Order"

class ViewModelFormModalMmTechnologicOrders(ViewModelFormModalController):
	_name = "form.modal:mm.technologic.orders"
	_view_name = "mm.technologic.orders/form.modal"
	_description = "Technologic Order"

class ViewModelFormMmTechnologicOrders(ViewModelFormController):
	_name = "form:mm.technologic.orders"
	_view_name = "mm.technologic.orders/form"
	_description = "Technologic Order"

class ViewModelGanttMmTechnologicOrders(ViewModelGanttController):
	_name = "gantt:mm.technologic.orders"
	_view_name = "mm.technologic.orders/gantt"
	_description = "Technologic Order"

class ViewModelScheduleMmTechnologicOrders(ViewModelScheduleController):
	_name = "schedule:mm.technologic.orders"
	_view_name = "mm.technologic.orders/schedule"
	_description = "Technologic Order"

class ViewModelCalendarMmTechnologicOrders(ViewModelCalendarController):
	_name = "calendar:mm.technologic.orders"
	_view_name = "mm.technologic.orders/calendar"
	_description = "Technologic Order"

class ViewModelGraphMmTechnologicOrders(ViewModelGraphController):
	_name = "graph:mm.technologic.orders"
	_view_name = "mm.technologic.orders/graph"
	_description = "Technologic Order"

class ViewModelKanbanMmTechnologicOrders(ViewModelKanbanController):
	_name = "kanban:mm.technologic.orders"
	_view_name = "mm.technologic.orders/kanban"
	_description = "Technologic Order"

class ViewModelMdxMmTechnologicOrders(ViewModelMdxController):
	_name = "mdx:mm.technologic.orders"
	_view_name = "mm.technologic.orders/mdx"
	_description = "Technologic Order"
