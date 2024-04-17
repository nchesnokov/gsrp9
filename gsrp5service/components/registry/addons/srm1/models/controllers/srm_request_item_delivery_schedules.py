from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.request.item.delivery.schedules"
	_view_name = "srm.request.item.delivery.schedules/find"
	_description = "SRM Request Delivery Schedules"

class ViewModelO2MFormSrmRequestItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.item.delivery.schedules"
	_view_name = "srm.request.item.delivery.schedules/o2m-form"
	_description = "SRM Request Delivery Schedules"

class ViewModelO2MCalendarSrmRequestItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.request.item.delivery.schedules"
	_view_name = "srm.request.item.delivery.schedules/o2m-calendar"
	_description = "SRM Request Delivery Schedules"

class ViewModelO2MGraphSrmRequestItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.request.item.delivery.schedules"
	_view_name = "srm.request.item.delivery.schedules/o2m-graph"
	_description = "SRM Request Delivery Schedules"

class ViewModelO2MMdxSrmRequestItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.request.item.delivery.schedules"
	_view_name = "srm.request.item.delivery.schedules/o2m-mdx"
	_description = "SRM Request Delivery Schedules"

class ViewModelO2MListSrmRequestItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.request.item.delivery.schedules"
	_view_name = "srm.request.item.delivery.schedules/o2m-list"
	_description = "SRM Request Delivery Schedules"
