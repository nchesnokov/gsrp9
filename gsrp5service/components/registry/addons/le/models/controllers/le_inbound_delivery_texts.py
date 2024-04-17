from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryTexts(ViewModelFindController):
	_name = "find:le.inbound.delivery.texts"
	_view_name = "le.inbound.delivery.texts/find"
	_description = "Inbound Delivery Texts"

class ViewModelO2MFormLeInboundDeliveryTexts(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.texts"
	_view_name = "le.inbound.delivery.texts/o2m-form"
	_description = "Inbound Delivery Texts"

class ViewModelO2MListLeInboundDeliveryTexts(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.texts"
	_view_name = "le.inbound.delivery.texts/o2m-list"
	_description = "Inbound Delivery Texts"
