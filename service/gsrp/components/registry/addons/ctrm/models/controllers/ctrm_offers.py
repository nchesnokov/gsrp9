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

class ViewModelSearchCtrmOffers(ViewModelSearchController):
	_name = "search:ctrm.offers"
	_view_name = "ctrm.offers/search"
	_description = "CTRM Offer"

class ViewModelFindCtrmOffers(ViewModelFindController):
	_name = "find:ctrm.offers"
	_view_name = "ctrm.offers/find"
	_description = "CTRM Offer"

class ViewModelListCtrmOffers(ViewModelListController):
	_name = "list:ctrm.offers"
	_view_name = "ctrm.offers/list"
	_description = "CTRM Offer"

class ViewModelFormModalCtrmOffers(ViewModelFormModalController):
	_name = "form.modal:ctrm.offers"
	_view_name = "ctrm.offers/form.modal"
	_description = "CTRM Offer"

class ViewModelFormCtrmOffers(ViewModelFormController):
	_name = "form:ctrm.offers"
	_view_name = "ctrm.offers/form"
	_description = "CTRM Offer"

class ViewModelGanttCtrmOffers(ViewModelGanttController):
	_name = "gantt:ctrm.offers"
	_view_name = "ctrm.offers/gantt"
	_description = "CTRM Offer"

class ViewModelScheduleCtrmOffers(ViewModelScheduleController):
	_name = "schedule:ctrm.offers"
	_view_name = "ctrm.offers/schedule"
	_description = "CTRM Offer"

class ViewModelCalendarCtrmOffers(ViewModelCalendarController):
	_name = "calendar:ctrm.offers"
	_view_name = "ctrm.offers/calendar"
	_description = "CTRM Offer"

class ViewModelGraphCtrmOffers(ViewModelGraphController):
	_name = "graph:ctrm.offers"
	_view_name = "ctrm.offers/graph"
	_description = "CTRM Offer"

class ViewModelKanbanCtrmOffers(ViewModelKanbanController):
	_name = "kanban:ctrm.offers"
	_view_name = "ctrm.offers/kanban"
	_description = "CTRM Offer"

class ViewModelMdxCtrmOffers(ViewModelMdxController):
	_name = "mdx:ctrm.offers"
	_view_name = "ctrm.offers/mdx"
	_description = "CTRM Offer"
