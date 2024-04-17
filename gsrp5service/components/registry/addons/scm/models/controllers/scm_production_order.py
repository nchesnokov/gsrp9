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

class ViewModelSearchScmProductionOrder(ViewModelSearchController):
	_name = "search:scm.production.order"
	_view_name = "scm.production.order/search"
	_description = "Production Order"

class ViewModelFindScmProductionOrder(ViewModelFindController):
	_name = "find:scm.production.order"
	_view_name = "scm.production.order/find"
	_description = "Production Order"

class ViewModelListScmProductionOrder(ViewModelListController):
	_name = "list:scm.production.order"
	_view_name = "scm.production.order/list"
	_description = "Production Order"

class ViewModelFormModalScmProductionOrder(ViewModelFormModalController):
	_name = "form.modal:scm.production.order"
	_view_name = "scm.production.order/form.modal"
	_description = "Production Order"

class ViewModelFormScmProductionOrder(ViewModelFormController):
	_name = "form:scm.production.order"
	_view_name = "scm.production.order/form"
	_description = "Production Order"

class ViewModelGanttScmProductionOrder(ViewModelGanttController):
	_name = "gantt:scm.production.order"
	_view_name = "scm.production.order/gantt"
	_description = "Production Order"

class ViewModelScheduleScmProductionOrder(ViewModelScheduleController):
	_name = "schedule:scm.production.order"
	_view_name = "scm.production.order/schedule"
	_description = "Production Order"

class ViewModelCalendarScmProductionOrder(ViewModelCalendarController):
	_name = "calendar:scm.production.order"
	_view_name = "scm.production.order/calendar"
	_description = "Production Order"

class ViewModelGraphScmProductionOrder(ViewModelGraphController):
	_name = "graph:scm.production.order"
	_view_name = "scm.production.order/graph"
	_description = "Production Order"

class ViewModelKanbanScmProductionOrder(ViewModelKanbanController):
	_name = "kanban:scm.production.order"
	_view_name = "scm.production.order/kanban"
	_description = "Production Order"

class ViewModelMdxScmProductionOrder(ViewModelMdxController):
	_name = "mdx:scm.production.order"
	_view_name = "scm.production.order/mdx"
	_description = "Production Order"
