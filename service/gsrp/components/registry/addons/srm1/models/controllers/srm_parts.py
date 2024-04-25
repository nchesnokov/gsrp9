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

class ViewModelSearchSrmParts(ViewModelSearchController):
	_name = "search:srm.parts"
	_view_name = "srm.parts/search"
	_description = "SRM Part"

class ViewModelFindSrmParts(ViewModelFindController):
	_name = "find:srm.parts"
	_view_name = "srm.parts/find"
	_description = "SRM Part"

class ViewModelListSrmParts(ViewModelListController):
	_name = "list:srm.parts"
	_view_name = "srm.parts/list"
	_description = "SRM Part"

class ViewModelFormModalSrmParts(ViewModelFormModalController):
	_name = "form.modal:srm.parts"
	_view_name = "srm.parts/form.modal"
	_description = "SRM Part"

class ViewModelFormSrmParts(ViewModelFormController):
	_name = "form:srm.parts"
	_view_name = "srm.parts/form"
	_description = "SRM Part"

class ViewModelGanttSrmParts(ViewModelGanttController):
	_name = "gantt:srm.parts"
	_view_name = "srm.parts/gantt"
	_description = "SRM Part"

class ViewModelScheduleSrmParts(ViewModelScheduleController):
	_name = "schedule:srm.parts"
	_view_name = "srm.parts/schedule"
	_description = "SRM Part"

class ViewModelCalendarSrmParts(ViewModelCalendarController):
	_name = "calendar:srm.parts"
	_view_name = "srm.parts/calendar"
	_description = "SRM Part"

class ViewModelGraphSrmParts(ViewModelGraphController):
	_name = "graph:srm.parts"
	_view_name = "srm.parts/graph"
	_description = "SRM Part"

class ViewModelMdxSrmParts(ViewModelMdxController):
	_name = "mdx:srm.parts"
	_view_name = "srm.parts/mdx"
	_description = "SRM Part"
