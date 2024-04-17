from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInternalDeliveryTexts(ViewModelFindController):
	_name = "find:le.internal.delivery.texts"
	_view_name = "le.internal.delivery.texts/find"
	_description = "Internal Delivery Texts"

class ViewModelO2MFormLeInternalDeliveryTexts(ViewModelO2MFormController):
	_name = "o2m-form:le.internal.delivery.texts"
	_view_name = "le.internal.delivery.texts/o2m-form"
	_description = "Internal Delivery Texts"

class ViewModelO2MListLeInternalDeliveryTexts(ViewModelO2MListController):
	_name = "o2m-list:le.internal.delivery.texts"
	_view_name = "le.internal.delivery.texts/o2m-list"
	_description = "Internal Delivery Texts"
