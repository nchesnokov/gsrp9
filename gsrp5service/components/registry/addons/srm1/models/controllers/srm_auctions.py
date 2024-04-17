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

class ViewModelSearchSrmAuctions(ViewModelSearchController):
	_name = "search:srm.auctions"
	_view_name = "srm.auctions/search"
	_description = "SRM Auction"

class ViewModelFindSrmAuctions(ViewModelFindController):
	_name = "find:srm.auctions"
	_view_name = "srm.auctions/find"
	_description = "SRM Auction"

class ViewModelListSrmAuctions(ViewModelListController):
	_name = "list:srm.auctions"
	_view_name = "srm.auctions/list"
	_description = "SRM Auction"

class ViewModelFormModalSrmAuctions(ViewModelFormModalController):
	_name = "form.modal:srm.auctions"
	_view_name = "srm.auctions/form.modal"
	_description = "SRM Auction"

class ViewModelFormSrmAuctions(ViewModelFormController):
	_name = "form:srm.auctions"
	_view_name = "srm.auctions/form"
	_description = "SRM Auction"

class ViewModelGanttSrmAuctions(ViewModelGanttController):
	_name = "gantt:srm.auctions"
	_view_name = "srm.auctions/gantt"
	_description = "SRM Auction"

class ViewModelScheduleSrmAuctions(ViewModelScheduleController):
	_name = "schedule:srm.auctions"
	_view_name = "srm.auctions/schedule"
	_description = "SRM Auction"

class ViewModelCalendarSrmAuctions(ViewModelCalendarController):
	_name = "calendar:srm.auctions"
	_view_name = "srm.auctions/calendar"
	_description = "SRM Auction"

class ViewModelGraphSrmAuctions(ViewModelGraphController):
	_name = "graph:srm.auctions"
	_view_name = "srm.auctions/graph"
	_description = "SRM Auction"

class ViewModelMdxSrmAuctions(ViewModelMdxController):
	_name = "mdx:srm.auctions"
	_view_name = "srm.auctions/mdx"
	_description = "SRM Auction"
