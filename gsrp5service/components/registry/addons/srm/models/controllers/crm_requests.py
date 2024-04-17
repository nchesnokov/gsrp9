from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGanttController
from gsrp5service.obj.controller.controller import ViewModelScheduleController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchCrmRequests(ViewModelSearchController):
	_name = "search:crm.requests"
	_view_name = "crm.requests/search"
	_description = "CRM Requests"

class ViewModelFindCrmRequests(ViewModelFindController):
	_name = "find:crm.requests"
	_view_name = "crm.requests/find"
	_description = "CRM Requests"

class ViewModelListCrmRequests(ViewModelListController):
	_name = "list:crm.requests"
	_view_name = "crm.requests/list"
	_description = "CRM Requests"

class ViewModelFormModalCrmRequests(ViewModelFormModalController):
	_name = "form.modal:crm.requests"
	_view_name = "crm.requests/form.modal"
	_description = "CRM Requests"

class ViewModelFormCrmRequests(ViewModelFormController):
	_name = "form:crm.requests"
	_view_name = "crm.requests/form"
	_description = "CRM Requests"

class ViewModelGanttCrmRequests(ViewModelGanttController):
	_name = "gantt:crm.requests"
	_view_name = "crm.requests/gantt"
	_description = "CRM Requests"

class ViewModelScheduleCrmRequests(ViewModelScheduleController):
	_name = "schedule:crm.requests"
	_view_name = "crm.requests/schedule"
	_description = "CRM Requests"

class ViewModelCalendarCrmRequests(ViewModelCalendarController):
	_name = "calendar:crm.requests"
	_view_name = "crm.requests/calendar"
	_description = "CRM Requests"

class ViewModelGraphCrmRequests(ViewModelGraphController):
	_name = "graph:crm.requests"
	_view_name = "crm.requests/graph"
	_description = "CRM Requests"

class ViewModelMdxCrmRequests(ViewModelMdxController):
	_name = "mdx:crm.requests"
	_view_name = "crm.requests/mdx"
	_description = "CRM Requests"
