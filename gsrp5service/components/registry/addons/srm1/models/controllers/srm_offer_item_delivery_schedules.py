from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.offer.item.delivery.schedules"
	_view_name = "srm.offer.item.delivery.schedules/find"
	_description = "SRM Offer Delivery Schedules"

class ViewModelO2MFormSrmOfferItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.item.delivery.schedules"
	_view_name = "srm.offer.item.delivery.schedules/o2m-form"
	_description = "SRM Offer Delivery Schedules"

class ViewModelO2MCalendarSrmOfferItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.offer.item.delivery.schedules"
	_view_name = "srm.offer.item.delivery.schedules/o2m-calendar"
	_description = "SRM Offer Delivery Schedules"

class ViewModelO2MGraphSrmOfferItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.offer.item.delivery.schedules"
	_view_name = "srm.offer.item.delivery.schedules/o2m-graph"
	_description = "SRM Offer Delivery Schedules"

class ViewModelO2MMdxSrmOfferItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.offer.item.delivery.schedules"
	_view_name = "srm.offer.item.delivery.schedules/o2m-mdx"
	_description = "SRM Offer Delivery Schedules"

class ViewModelO2MListSrmOfferItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.item.delivery.schedules"
	_view_name = "srm.offer.item.delivery.schedules/o2m-list"
	_description = "SRM Offer Delivery Schedules"
