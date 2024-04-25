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

class ViewModelSearchPurchaseOrders(ViewModelSearchController):
	_name = "search:purchase.orders"
	_view_name = "purchase.orders/search"
	_description = "Purchase Order"

class ViewModelFindPurchaseOrders(ViewModelFindController):
	_name = "find:purchase.orders"
	_view_name = "purchase.orders/find"
	_description = "Purchase Order"

class ViewModelListPurchaseOrders(ViewModelListController):
	_name = "list:purchase.orders"
	_view_name = "purchase.orders/list"
	_description = "Purchase Order"

class ViewModelFormModalPurchaseOrders(ViewModelFormModalController):
	_name = "form.modal:purchase.orders"
	_view_name = "purchase.orders/form.modal"
	_description = "Purchase Order"

class ViewModelFormPurchaseOrders(ViewModelFormController):
	_name = "form:purchase.orders"
	_view_name = "purchase.orders/form"
	_description = "Purchase Order"

class ViewModelGanttPurchaseOrders(ViewModelGanttController):
	_name = "gantt:purchase.orders"
	_view_name = "purchase.orders/gantt"
	_description = "Purchase Order"

class ViewModelSchedulePurchaseOrders(ViewModelScheduleController):
	_name = "schedule:purchase.orders"
	_view_name = "purchase.orders/schedule"
	_description = "Purchase Order"

class ViewModelCalendarPurchaseOrders(ViewModelCalendarController):
	_name = "calendar:purchase.orders"
	_view_name = "purchase.orders/calendar"
	_description = "Purchase Order"

class ViewModelGraphPurchaseOrders(ViewModelGraphController):
	_name = "graph:purchase.orders"
	_view_name = "purchase.orders/graph"
	_description = "Purchase Order"

class ViewModelKanbanPurchaseOrders(ViewModelKanbanController):
	_name = "kanban:purchase.orders"
	_view_name = "purchase.orders/kanban"
	_description = "Purchase Order"

class ViewModelMdxPurchaseOrders(ViewModelMdxController):
	_name = "mdx:purchase.orders"
	_view_name = "purchase.orders/mdx"
	_description = "Purchase Order"
