from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeOutboundDeliveryItemTexts(ViewModelFindController):
	_name = "find:le.outbound.delivery.item.texts"
	_view_name = "le.outbound.delivery.item.texts/find"
	_description = "Outbound Delivery Texts"

class ViewModelO2MFormLeOutboundDeliveryItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:le.outbound.delivery.item.texts"
	_view_name = "le.outbound.delivery.item.texts/o2m-form"
	_description = "Outbound Delivery Texts"

class ViewModelO2MListLeOutboundDeliveryItemTexts(ViewModelO2MListController):
	_name = "o2m-list:le.outbound.delivery.item.texts"
	_view_name = "le.outbound.delivery.item.texts/o2m-list"
	_description = "Outbound Delivery Texts"
