from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeOutboundDeliveryTexts(ViewModelFindController):
	_name = "find:le.outbound.delivery.texts"
	_view_name = "le.outbound.delivery.texts/find"
	_description = "Outbound Delivery Texts"

class ViewModelO2MFormLeOutboundDeliveryTexts(ViewModelO2MFormController):
	_name = "o2m-form:le.outbound.delivery.texts"
	_view_name = "le.outbound.delivery.texts/o2m-form"
	_description = "Outbound Delivery Texts"

class ViewModelO2MListLeOutboundDeliveryTexts(ViewModelO2MListController):
	_name = "o2m-list:le.outbound.delivery.texts"
	_view_name = "le.outbound.delivery.texts/o2m-list"
	_description = "Outbound Delivery Texts"
