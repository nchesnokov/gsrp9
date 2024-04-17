from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmOfferItemDeliverySchedules(ViewModelFindController):
	_name = "find:ctrm.offer.item.delivery.schedules"
	_view_name = "ctrm.offer.item.delivery.schedules/find"
	_description = "CTRM Offer Item Delivery Schedules"

class ViewModelO2MFormCtrmOfferItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.offer.item.delivery.schedules"
	_view_name = "ctrm.offer.item.delivery.schedules/o2m-form"
	_description = "CTRM Offer Item Delivery Schedules"

class ViewModelO2MListCtrmOfferItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:ctrm.offer.item.delivery.schedules"
	_view_name = "ctrm.offer.item.delivery.schedules/o2m-list"
	_description = "CTRM Offer Item Delivery Schedules"
