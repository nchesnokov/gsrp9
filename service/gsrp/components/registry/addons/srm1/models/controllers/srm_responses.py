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

class ViewModelSearchSrmResponses(ViewModelSearchController):
	_name = "search:srm.responses"
	_view_name = "srm.responses/search"
	_description = "SRM Response"

class ViewModelFindSrmResponses(ViewModelFindController):
	_name = "find:srm.responses"
	_view_name = "srm.responses/find"
	_description = "SRM Response"

class ViewModelListSrmResponses(ViewModelListController):
	_name = "list:srm.responses"
	_view_name = "srm.responses/list"
	_description = "SRM Response"

class ViewModelFormModalSrmResponses(ViewModelFormModalController):
	_name = "form.modal:srm.responses"
	_view_name = "srm.responses/form.modal"
	_description = "SRM Response"

class ViewModelFormSrmResponses(ViewModelFormController):
	_name = "form:srm.responses"
	_view_name = "srm.responses/form"
	_description = "SRM Response"

class ViewModelGanttSrmResponses(ViewModelGanttController):
	_name = "gantt:srm.responses"
	_view_name = "srm.responses/gantt"
	_description = "SRM Response"

class ViewModelScheduleSrmResponses(ViewModelScheduleController):
	_name = "schedule:srm.responses"
	_view_name = "srm.responses/schedule"
	_description = "SRM Response"

class ViewModelCalendarSrmResponses(ViewModelCalendarController):
	_name = "calendar:srm.responses"
	_view_name = "srm.responses/calendar"
	_description = "SRM Response"

class ViewModelGraphSrmResponses(ViewModelGraphController):
	_name = "graph:srm.responses"
	_view_name = "srm.responses/graph"
	_description = "SRM Response"

class ViewModelMdxSrmResponses(ViewModelMdxController):
	_name = "mdx:srm.responses"
	_view_name = "srm.responses/mdx"
	_description = "SRM Response"
