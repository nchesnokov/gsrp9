from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOfferItemDeliverySchedules(ViewModelFindController):
	_name = "find:crm.offer.item.delivery.schedules"
	_view_name = "crm.offer.item.delivery.schedules/find"
	_description = "CRM Offer Item Delivery Schedules"

class ViewModelO2MFormCrmOfferItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.offer.item.delivery.schedules"
	_view_name = "crm.offer.item.delivery.schedules/o2m-form"
	_description = "CRM Offer Item Delivery Schedules"

class ViewModelO2MListCrmOfferItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.offer.item.delivery.schedules"
	_view_name = "crm.offer.item.delivery.schedules/o2m-list"
	_description = "CRM Offer Item Delivery Schedules"
