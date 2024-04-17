from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeInboundDeliveryTypes(ViewModelSearchController):
	_name = "search:le.inbound.delivery.types"
	_view_name = "le.inbound.delivery.types/search"
	_description = "Types Inbound Delivery"

class ViewModelFindLeInboundDeliveryTypes(ViewModelFindController):
	_name = "find:le.inbound.delivery.types"
	_view_name = "le.inbound.delivery.types/find"
	_description = "Types Inbound Delivery"

class ViewModelListLeInboundDeliveryTypes(ViewModelListController):
	_name = "list:le.inbound.delivery.types"
	_view_name = "le.inbound.delivery.types/list"
	_description = "Types Inbound Delivery"

class ViewModelFormModalLeInboundDeliveryTypes(ViewModelFormModalController):
	_name = "form.modal:le.inbound.delivery.types"
	_view_name = "le.inbound.delivery.types/form.modal"
	_description = "Types Inbound Delivery"

class ViewModelFormLeInboundDeliveryTypes(ViewModelFormController):
	_name = "form:le.inbound.delivery.types"
	_view_name = "le.inbound.delivery.types/form"
	_description = "Types Inbound Delivery"
