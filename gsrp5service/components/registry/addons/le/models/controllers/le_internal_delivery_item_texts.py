from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInternalDeliveryItemTexts(ViewModelFindController):
	_name = "find:le.internal.delivery.item.texts"
	_view_name = "le.internal.delivery.item.texts/find"
	_description = "Inbound Delivery Texts"

class ViewModelO2MFormLeInternalDeliveryItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:le.internal.delivery.item.texts"
	_view_name = "le.internal.delivery.item.texts/o2m-form"
	_description = "Inbound Delivery Texts"

class ViewModelO2MListLeInternalDeliveryItemTexts(ViewModelO2MListController):
	_name = "o2m-list:le.internal.delivery.item.texts"
	_view_name = "le.internal.delivery.item.texts/o2m-list"
	_description = "Inbound Delivery Texts"
