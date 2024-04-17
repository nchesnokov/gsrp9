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

class ViewModelSearchSaleOrders(ViewModelSearchController):
	_name = "search:sale.orders"
	_view_name = "sale.orders/search"
	_description = "Sale Orders"

class ViewModelFindSaleOrders(ViewModelFindController):
	_name = "find:sale.orders"
	_view_name = "sale.orders/find"
	_description = "Sale Orders"

class ViewModelListSaleOrders(ViewModelListController):
	_name = "list:sale.orders"
	_view_name = "sale.orders/list"
	_description = "Sale Orders"

class ViewModelFormModalSaleOrders(ViewModelFormModalController):
	_name = "form.modal:sale.orders"
	_view_name = "sale.orders/form.modal"
	_description = "Sale Orders"

class ViewModelFormSaleOrders(ViewModelFormController):
	_name = "form:sale.orders"
	_view_name = "sale.orders/form"
	_description = "Sale Orders"

class ViewModelGanttSaleOrders(ViewModelGanttController):
	_name = "gantt:sale.orders"
	_view_name = "sale.orders/gantt"
	_description = "Sale Orders"

class ViewModelScheduleSaleOrders(ViewModelScheduleController):
	_name = "schedule:sale.orders"
	_view_name = "sale.orders/schedule"
	_description = "Sale Orders"

class ViewModelCalendarSaleOrders(ViewModelCalendarController):
	_name = "calendar:sale.orders"
	_view_name = "sale.orders/calendar"
	_description = "Sale Orders"

class ViewModelGraphSaleOrders(ViewModelGraphController):
	_name = "graph:sale.orders"
	_view_name = "sale.orders/graph"
	_description = "Sale Orders"

class ViewModelKanbanSaleOrders(ViewModelKanbanController):
	_name = "kanban:sale.orders"
	_view_name = "sale.orders/kanban"
	_description = "Sale Orders"

class ViewModelMdxSaleOrders(ViewModelMdxController):
	_name = "mdx:sale.orders"
	_view_name = "sale.orders/mdx"
	_description = "Sale Orders"
