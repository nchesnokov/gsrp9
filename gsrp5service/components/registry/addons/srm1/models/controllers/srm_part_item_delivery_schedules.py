from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.part.item.delivery.schedules"
	_view_name = "srm.part.item.delivery.schedules/find"
	_description = "SRM Part Delivery Schedules"

class ViewModelO2MFormSrmPartItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.item.delivery.schedules"
	_view_name = "srm.part.item.delivery.schedules/o2m-form"
	_description = "SRM Part Delivery Schedules"

class ViewModelO2MCalendarSrmPartItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.part.item.delivery.schedules"
	_view_name = "srm.part.item.delivery.schedules/o2m-calendar"
	_description = "SRM Part Delivery Schedules"

class ViewModelO2MGraphSrmPartItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.part.item.delivery.schedules"
	_view_name = "srm.part.item.delivery.schedules/o2m-graph"
	_description = "SRM Part Delivery Schedules"

class ViewModelO2MMdxSrmPartItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.part.item.delivery.schedules"
	_view_name = "srm.part.item.delivery.schedules/o2m-mdx"
	_description = "SRM Part Delivery Schedules"

class ViewModelO2MListSrmPartItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.part.item.delivery.schedules"
	_view_name = "srm.part.item.delivery.schedules/o2m-list"
	_description = "SRM Part Delivery Schedules"
