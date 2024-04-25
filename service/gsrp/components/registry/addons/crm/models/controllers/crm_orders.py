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

class ViewModelSearchCrmOrders(ViewModelSearchController):
	_name = "search:crm.orders"
	_view_name = "crm.orders/search"
	_description = "CRM Orders"

class ViewModelFindCrmOrders(ViewModelFindController):
	_name = "find:crm.orders"
	_view_name = "crm.orders/find"
	_description = "CRM Orders"

class ViewModelListCrmOrders(ViewModelListController):
	_name = "list:crm.orders"
	_view_name = "crm.orders/list"
	_description = "CRM Orders"

class ViewModelFormModalCrmOrders(ViewModelFormModalController):
	_name = "form.modal:crm.orders"
	_view_name = "crm.orders/form.modal"
	_description = "CRM Orders"

class ViewModelFormCrmOrders(ViewModelFormController):
	_name = "form:crm.orders"
	_view_name = "crm.orders/form"
	_description = "CRM Orders"

class ViewModelGanttCrmOrders(ViewModelGanttController):
	_name = "gantt:crm.orders"
	_view_name = "crm.orders/gantt"
	_description = "CRM Orders"

class ViewModelScheduleCrmOrders(ViewModelScheduleController):
	_name = "schedule:crm.orders"
	_view_name = "crm.orders/schedule"
	_description = "CRM Orders"

class ViewModelCalendarCrmOrders(ViewModelCalendarController):
	_name = "calendar:crm.orders"
	_view_name = "crm.orders/calendar"
	_description = "CRM Orders"

class ViewModelGraphCrmOrders(ViewModelGraphController):
	_name = "graph:crm.orders"
	_view_name = "crm.orders/graph"
	_description = "CRM Orders"

class ViewModelKanbanCrmOrders(ViewModelKanbanController):
	_name = "kanban:crm.orders"
	_view_name = "crm.orders/kanban"
	_description = "CRM Orders"

class ViewModelMdxCrmOrders(ViewModelMdxController):
	_name = "mdx:crm.orders"
	_view_name = "crm.orders/mdx"
	_description = "CRM Orders"
