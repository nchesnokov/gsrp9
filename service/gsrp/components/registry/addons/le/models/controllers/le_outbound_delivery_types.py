from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeOutboundDeliveryTypes(ViewModelSearchController):
	_name = "search:le.outbound.delivery.types"
	_view_name = "le.outbound.delivery.types/search"
	_description = "Types Outbound Delivery"

class ViewModelFindLeOutboundDeliveryTypes(ViewModelFindController):
	_name = "find:le.outbound.delivery.types"
	_view_name = "le.outbound.delivery.types/find"
	_description = "Types Outbound Delivery"

class ViewModelListLeOutboundDeliveryTypes(ViewModelListController):
	_name = "list:le.outbound.delivery.types"
	_view_name = "le.outbound.delivery.types/list"
	_description = "Types Outbound Delivery"

class ViewModelFormModalLeOutboundDeliveryTypes(ViewModelFormModalController):
	_name = "form.modal:le.outbound.delivery.types"
	_view_name = "le.outbound.delivery.types/form.modal"
	_description = "Types Outbound Delivery"

class ViewModelFormLeOutboundDeliveryTypes(ViewModelFormController):
	_name = "form:le.outbound.delivery.types"
	_view_name = "le.outbound.delivery.types/form"
	_description = "Types Outbound Delivery"
