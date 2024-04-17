from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeInternalDeliveryTypes(ViewModelSearchController):
	_name = "search:le.internal.delivery.types"
	_view_name = "le.internal.delivery.types/search"
	_description = "Types Internal Delivery"

class ViewModelFindLeInternalDeliveryTypes(ViewModelFindController):
	_name = "find:le.internal.delivery.types"
	_view_name = "le.internal.delivery.types/find"
	_description = "Types Internal Delivery"

class ViewModelListLeInternalDeliveryTypes(ViewModelListController):
	_name = "list:le.internal.delivery.types"
	_view_name = "le.internal.delivery.types/list"
	_description = "Types Internal Delivery"

class ViewModelFormModalLeInternalDeliveryTypes(ViewModelFormModalController):
	_name = "form.modal:le.internal.delivery.types"
	_view_name = "le.internal.delivery.types/form.modal"
	_description = "Types Internal Delivery"

class ViewModelFormLeInternalDeliveryTypes(ViewModelFormController):
	_name = "form:le.internal.delivery.types"
	_view_name = "le.internal.delivery.types/form"
	_description = "Types Internal Delivery"
