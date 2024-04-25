from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferDeadlines(ViewModelFindController):
	_name = "find:srm.offer.deadlines"
	_view_name = "srm.offer.deadlines/find"
	_description = "SRM Offer Deadlines"

class ViewModelO2MFormSrmOfferDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.deadlines"
	_view_name = "srm.offer.deadlines/o2m-form"
	_description = "SRM Offer Deadlines"

class ViewModelO2MGanttSrmOfferDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.offer.deadlines"
	_view_name = "srm.offer.deadlines/o2m-gantt"
	_description = "SRM Offer Deadlines"

class ViewModelO2MScheduleSrmOfferDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.offer.deadlines"
	_view_name = "srm.offer.deadlines/o2m-schedule"
	_description = "SRM Offer Deadlines"

class ViewModelO2MListSrmOfferDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.deadlines"
	_view_name = "srm.offer.deadlines/o2m-list"
	_description = "SRM Offer Deadlines"
