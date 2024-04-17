from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInternalDeliveryItems(ViewModelFindController):
	_name = "find:le.internal.delivery.items"
	_view_name = "le.internal.delivery.items/find"
	_description = "Internal Delivery Items"

class ViewModelO2MFormLeInternalDeliveryItems(ViewModelO2MFormController):
	_name = "o2m-form:le.internal.delivery.items"
	_view_name = "le.internal.delivery.items/o2m-form"
	_description = "Internal Delivery Items"

class ViewModelO2MListLeInternalDeliveryItems(ViewModelO2MListController):
	_name = "o2m-list:le.internal.delivery.items"
	_view_name = "le.internal.delivery.items/o2m-list"
	_description = "Internal Delivery Items"
