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

class ViewModelSearchSrmRequests(ViewModelSearchController):
	_name = "search:srm.requests"
	_view_name = "srm.requests/search"
	_description = "SRM Request"

class ViewModelFindSrmRequests(ViewModelFindController):
	_name = "find:srm.requests"
	_view_name = "srm.requests/find"
	_description = "SRM Request"

class ViewModelListSrmRequests(ViewModelListController):
	_name = "list:srm.requests"
	_view_name = "srm.requests/list"
	_description = "SRM Request"

class ViewModelFormModalSrmRequests(ViewModelFormModalController):
	_name = "form.modal:srm.requests"
	_view_name = "srm.requests/form.modal"
	_description = "SRM Request"

class ViewModelFormSrmRequests(ViewModelFormController):
	_name = "form:srm.requests"
	_view_name = "srm.requests/form"
	_description = "SRM Request"

class ViewModelGanttSrmRequests(ViewModelGanttController):
	_name = "gantt:srm.requests"
	_view_name = "srm.requests/gantt"
	_description = "SRM Request"

class ViewModelScheduleSrmRequests(ViewModelScheduleController):
	_name = "schedule:srm.requests"
	_view_name = "srm.requests/schedule"
	_description = "SRM Request"

class ViewModelCalendarSrmRequests(ViewModelCalendarController):
	_name = "calendar:srm.requests"
	_view_name = "srm.requests/calendar"
	_description = "SRM Request"

class ViewModelGraphSrmRequests(ViewModelGraphController):
	_name = "graph:srm.requests"
	_view_name = "srm.requests/graph"
	_description = "SRM Request"

class ViewModelMdxSrmRequests(ViewModelMdxController):
	_name = "mdx:srm.requests"
	_view_name = "srm.requests/mdx"
	_description = "SRM Request"
