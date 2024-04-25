from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryItems(ViewModelFindController):
	_name = "find:le.inbound.delivery.items"
	_view_name = "le.inbound.delivery.items/find"
	_description = "Inbound Delivery Items"

class ViewModelO2MFormLeInboundDeliveryItems(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.items"
	_view_name = "le.inbound.delivery.items/o2m-form"
	_description = "Inbound Delivery Items"

class ViewModelO2MListLeInboundDeliveryItems(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.items"
	_view_name = "le.inbound.delivery.items/o2m-list"
	_description = "Inbound Delivery Items"
