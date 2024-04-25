from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.rfx.item.delivery.schedules"
	_view_name = "srm.rfx.item.delivery.schedules/find"
	_description = "SRM RFX Delivery Schedules"

class ViewModelO2MFormSrmRfxItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.item.delivery.schedules"
	_view_name = "srm.rfx.item.delivery.schedules/o2m-form"
	_description = "SRM RFX Delivery Schedules"

class ViewModelO2MCalendarSrmRfxItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.rfx.item.delivery.schedules"
	_view_name = "srm.rfx.item.delivery.schedules/o2m-calendar"
	_description = "SRM RFX Delivery Schedules"

class ViewModelO2MGraphSrmRfxItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.rfx.item.delivery.schedules"
	_view_name = "srm.rfx.item.delivery.schedules/o2m-graph"
	_description = "SRM RFX Delivery Schedules"

class ViewModelO2MMdxSrmRfxItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.rfx.item.delivery.schedules"
	_view_name = "srm.rfx.item.delivery.schedules/o2m-mdx"
	_description = "SRM RFX Delivery Schedules"

class ViewModelO2MListSrmRfxItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.item.delivery.schedules"
	_view_name = "srm.rfx.item.delivery.schedules/o2m-list"
	_description = "SRM RFX Delivery Schedules"
