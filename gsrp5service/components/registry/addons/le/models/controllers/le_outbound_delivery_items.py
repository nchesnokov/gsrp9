from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeOutboundDeliveryItems(ViewModelFindController):
	_name = "find:le.outbound.delivery.items"
	_view_name = "le.outbound.delivery.items/find"
	_description = "Outbound Delivery Items"

class ViewModelO2MFormLeOutboundDeliveryItems(ViewModelO2MFormController):
	_name = "o2m-form:le.outbound.delivery.items"
	_view_name = "le.outbound.delivery.items/o2m-form"
	_description = "Outbound Delivery Items"

class ViewModelO2MListLeOutboundDeliveryItems(ViewModelO2MListController):
	_name = "o2m-list:le.outbound.delivery.items"
	_view_name = "le.outbound.delivery.items/o2m-list"
	_description = "Outbound Delivery Items"
