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

class ViewModelSearchSrmDecisions(ViewModelSearchController):
	_name = "search:srm.decisions"
	_view_name = "srm.decisions/search"
	_description = "SRM Decision"

class ViewModelFindSrmDecisions(ViewModelFindController):
	_name = "find:srm.decisions"
	_view_name = "srm.decisions/find"
	_description = "SRM Decision"

class ViewModelListSrmDecisions(ViewModelListController):
	_name = "list:srm.decisions"
	_view_name = "srm.decisions/list"
	_description = "SRM Decision"

class ViewModelFormModalSrmDecisions(ViewModelFormModalController):
	_name = "form.modal:srm.decisions"
	_view_name = "srm.decisions/form.modal"
	_description = "SRM Decision"

class ViewModelFormSrmDecisions(ViewModelFormController):
	_name = "form:srm.decisions"
	_view_name = "srm.decisions/form"
	_description = "SRM Decision"

class ViewModelGanttSrmDecisions(ViewModelGanttController):
	_name = "gantt:srm.decisions"
	_view_name = "srm.decisions/gantt"
	_description = "SRM Decision"

class ViewModelScheduleSrmDecisions(ViewModelScheduleController):
	_name = "schedule:srm.decisions"
	_view_name = "srm.decisions/schedule"
	_description = "SRM Decision"

class ViewModelCalendarSrmDecisions(ViewModelCalendarController):
	_name = "calendar:srm.decisions"
	_view_name = "srm.decisions/calendar"
	_description = "SRM Decision"

class ViewModelGraphSrmDecisions(ViewModelGraphController):
	_name = "graph:srm.decisions"
	_view_name = "srm.decisions/graph"
	_description = "SRM Decision"

class ViewModelMdxSrmDecisions(ViewModelMdxController):
	_name = "mdx:srm.decisions"
	_view_name = "srm.decisions/mdx"
	_description = "SRM Decision"
