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

class ViewModelSearchSrmRfxs(ViewModelSearchController):
	_name = "search:srm.rfxs"
	_view_name = "srm.rfxs/search"
	_description = "SRM RFX"

class ViewModelFindSrmRfxs(ViewModelFindController):
	_name = "find:srm.rfxs"
	_view_name = "srm.rfxs/find"
	_description = "SRM RFX"

class ViewModelListSrmRfxs(ViewModelListController):
	_name = "list:srm.rfxs"
	_view_name = "srm.rfxs/list"
	_description = "SRM RFX"

class ViewModelFormModalSrmRfxs(ViewModelFormModalController):
	_name = "form.modal:srm.rfxs"
	_view_name = "srm.rfxs/form.modal"
	_description = "SRM RFX"

class ViewModelFormSrmRfxs(ViewModelFormController):
	_name = "form:srm.rfxs"
	_view_name = "srm.rfxs/form"
	_description = "SRM RFX"

class ViewModelGanttSrmRfxs(ViewModelGanttController):
	_name = "gantt:srm.rfxs"
	_view_name = "srm.rfxs/gantt"
	_description = "SRM RFX"

class ViewModelScheduleSrmRfxs(ViewModelScheduleController):
	_name = "schedule:srm.rfxs"
	_view_name = "srm.rfxs/schedule"
	_description = "SRM RFX"

class ViewModelCalendarSrmRfxs(ViewModelCalendarController):
	_name = "calendar:srm.rfxs"
	_view_name = "srm.rfxs/calendar"
	_description = "SRM RFX"

class ViewModelGraphSrmRfxs(ViewModelGraphController):
	_name = "graph:srm.rfxs"
	_view_name = "srm.rfxs/graph"
	_description = "SRM RFX"

class ViewModelMdxSrmRfxs(ViewModelMdxController):
	_name = "mdx:srm.rfxs"
	_view_name = "srm.rfxs/mdx"
	_description = "SRM RFX"
