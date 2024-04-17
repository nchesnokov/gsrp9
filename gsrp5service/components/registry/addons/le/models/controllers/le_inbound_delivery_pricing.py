from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryPricing(ViewModelFindController):
	_name = "find:le.inbound.delivery.pricing"
	_view_name = "le.inbound.delivery.pricing/find"
	_description = "Inbound Delivery Pricing"

class ViewModelO2MFormLeInboundDeliveryPricing(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.pricing"
	_view_name = "le.inbound.delivery.pricing/o2m-form"
	_description = "Inbound Delivery Pricing"

class ViewModelO2MListLeInboundDeliveryPricing(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.pricing"
	_view_name = "le.inbound.delivery.pricing/o2m-list"
	_description = "Inbound Delivery Pricing"
