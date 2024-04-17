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

class ViewModelSearchSrmOffers(ViewModelSearchController):
	_name = "search:srm.offers"
	_view_name = "srm.offers/search"
	_description = "SRM Offer"

class ViewModelFindSrmOffers(ViewModelFindController):
	_name = "find:srm.offers"
	_view_name = "srm.offers/find"
	_description = "SRM Offer"

class ViewModelListSrmOffers(ViewModelListController):
	_name = "list:srm.offers"
	_view_name = "srm.offers/list"
	_description = "SRM Offer"

class ViewModelFormModalSrmOffers(ViewModelFormModalController):
	_name = "form.modal:srm.offers"
	_view_name = "srm.offers/form.modal"
	_description = "SRM Offer"

class ViewModelFormSrmOffers(ViewModelFormController):
	_name = "form:srm.offers"
	_view_name = "srm.offers/form"
	_description = "SRM Offer"

class ViewModelGanttSrmOffers(ViewModelGanttController):
	_name = "gantt:srm.offers"
	_view_name = "srm.offers/gantt"
	_description = "SRM Offer"

class ViewModelScheduleSrmOffers(ViewModelScheduleController):
	_name = "schedule:srm.offers"
	_view_name = "srm.offers/schedule"
	_description = "SRM Offer"

class ViewModelCalendarSrmOffers(ViewModelCalendarController):
	_name = "calendar:srm.offers"
	_view_name = "srm.offers/calendar"
	_description = "SRM Offer"

class ViewModelGraphSrmOffers(ViewModelGraphController):
	_name = "graph:srm.offers"
	_view_name = "srm.offers/graph"
	_description = "SRM Offer"

class ViewModelMdxSrmOffers(ViewModelMdxController):
	_name = "mdx:srm.offers"
	_view_name = "srm.offers/mdx"
	_description = "SRM Offer"
