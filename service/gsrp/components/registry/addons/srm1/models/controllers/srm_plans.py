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

class ViewModelSearchSrmPlans(ViewModelSearchController):
	_name = "search:srm.plans"
	_view_name = "srm.plans/search"
	_description = "SRM Plan"

class ViewModelFindSrmPlans(ViewModelFindController):
	_name = "find:srm.plans"
	_view_name = "srm.plans/find"
	_description = "SRM Plan"

class ViewModelListSrmPlans(ViewModelListController):
	_name = "list:srm.plans"
	_view_name = "srm.plans/list"
	_description = "SRM Plan"

class ViewModelFormModalSrmPlans(ViewModelFormModalController):
	_name = "form.modal:srm.plans"
	_view_name = "srm.plans/form.modal"
	_description = "SRM Plan"

class ViewModelFormSrmPlans(ViewModelFormController):
	_name = "form:srm.plans"
	_view_name = "srm.plans/form"
	_description = "SRM Plan"

class ViewModelGanttSrmPlans(ViewModelGanttController):
	_name = "gantt:srm.plans"
	_view_name = "srm.plans/gantt"
	_description = "SRM Plan"

class ViewModelScheduleSrmPlans(ViewModelScheduleController):
	_name = "schedule:srm.plans"
	_view_name = "srm.plans/schedule"
	_description = "SRM Plan"

class ViewModelCalendarSrmPlans(ViewModelCalendarController):
	_name = "calendar:srm.plans"
	_view_name = "srm.plans/calendar"
	_description = "SRM Plan"

class ViewModelGraphSrmPlans(ViewModelGraphController):
	_name = "graph:srm.plans"
	_view_name = "srm.plans/graph"
	_description = "SRM Plan"

class ViewModelMdxSrmPlans(ViewModelMdxController):
	_name = "mdx:srm.plans"
	_view_name = "srm.plans/mdx"
	_description = "SRM Plan"
