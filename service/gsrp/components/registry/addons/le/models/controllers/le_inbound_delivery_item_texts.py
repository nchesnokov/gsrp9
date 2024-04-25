from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryItemTexts(ViewModelFindController):
	_name = "find:le.inbound.delivery.item.texts"
	_view_name = "le.inbound.delivery.item.texts/find"
	_description = "Inbound Delivery Texts"

class ViewModelO2MFormLeInboundDeliveryItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.item.texts"
	_view_name = "le.inbound.delivery.item.texts/o2m-form"
	_description = "Inbound Delivery Texts"

class ViewModelO2MListLeInboundDeliveryItemTexts(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.item.texts"
	_view_name = "le.inbound.delivery.item.texts/o2m-list"
	_description = "Inbound Delivery Texts"
