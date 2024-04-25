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

class ViewModelSearchScmTechnologicOrder(ViewModelSearchController):
	_name = "search:scm.technologic.order"
	_view_name = "scm.technologic.order/search"
	_description = "Technologic Order"

class ViewModelFindScmTechnologicOrder(ViewModelFindController):
	_name = "find:scm.technologic.order"
	_view_name = "scm.technologic.order/find"
	_description = "Technologic Order"

class ViewModelListScmTechnologicOrder(ViewModelListController):
	_name = "list:scm.technologic.order"
	_view_name = "scm.technologic.order/list"
	_description = "Technologic Order"

class ViewModelFormModalScmTechnologicOrder(ViewModelFormModalController):
	_name = "form.modal:scm.technologic.order"
	_view_name = "scm.technologic.order/form.modal"
	_description = "Technologic Order"

class ViewModelFormScmTechnologicOrder(ViewModelFormController):
	_name = "form:scm.technologic.order"
	_view_name = "scm.technologic.order/form"
	_description = "Technologic Order"

class ViewModelGanttScmTechnologicOrder(ViewModelGanttController):
	_name = "gantt:scm.technologic.order"
	_view_name = "scm.technologic.order/gantt"
	_description = "Technologic Order"

class ViewModelScheduleScmTechnologicOrder(ViewModelScheduleController):
	_name = "schedule:scm.technologic.order"
	_view_name = "scm.technologic.order/schedule"
	_description = "Technologic Order"

class ViewModelCalendarScmTechnologicOrder(ViewModelCalendarController):
	_name = "calendar:scm.technologic.order"
	_view_name = "scm.technologic.order/calendar"
	_description = "Technologic Order"

class ViewModelGraphScmTechnologicOrder(ViewModelGraphController):
	_name = "graph:scm.technologic.order"
	_view_name = "scm.technologic.order/graph"
	_description = "Technologic Order"

class ViewModelKanbanScmTechnologicOrder(ViewModelKanbanController):
	_name = "kanban:scm.technologic.order"
	_view_name = "scm.technologic.order/kanban"
	_description = "Technologic Order"

class ViewModelMdxScmTechnologicOrder(ViewModelMdxController):
	_name = "mdx:scm.technologic.order"
	_view_name = "scm.technologic.order/mdx"
	_description = "Technologic Order"
