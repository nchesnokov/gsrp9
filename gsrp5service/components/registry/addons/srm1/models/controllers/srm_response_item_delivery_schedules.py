from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.response.item.delivery.schedules"
	_view_name = "srm.response.item.delivery.schedules/find"
	_description = "SRM Response Delivery Schedules"

class ViewModelO2MFormSrmResponseItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.item.delivery.schedules"
	_view_name = "srm.response.item.delivery.schedules/o2m-form"
	_description = "SRM Response Delivery Schedules"

class ViewModelO2MCalendarSrmResponseItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.response.item.delivery.schedules"
	_view_name = "srm.response.item.delivery.schedules/o2m-calendar"
	_description = "SRM Response Delivery Schedules"

class ViewModelO2MGraphSrmResponseItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.response.item.delivery.schedules"
	_view_name = "srm.response.item.delivery.schedules/o2m-graph"
	_description = "SRM Response Delivery Schedules"

class ViewModelO2MMdxSrmResponseItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.response.item.delivery.schedules"
	_view_name = "srm.response.item.delivery.schedules/o2m-mdx"
	_description = "SRM Response Delivery Schedules"

class ViewModelO2MListSrmResponseItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.response.item.delivery.schedules"
	_view_name = "srm.response.item.delivery.schedules/o2m-list"
	_description = "SRM Response Delivery Schedules"
