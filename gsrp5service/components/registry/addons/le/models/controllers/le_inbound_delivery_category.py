from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchLeInboundDeliveryCategory(ViewModelSearchController):
	_name = "search:le.inbound.delivery.category"
	_view_name = "le.inbound.delivery.category/search"
	_description = "Category Inbound Delivery"

class ViewModelFindLeInboundDeliveryCategory(ViewModelFindController):
	_name = "find:le.inbound.delivery.category"
	_view_name = "le.inbound.delivery.category/find"
	_description = "Category Inbound Delivery"

class ViewModelListLeInboundDeliveryCategory(ViewModelListController):
	_name = "list:le.inbound.delivery.category"
	_view_name = "le.inbound.delivery.category/list"
	_description = "Category Inbound Delivery"

class ViewModelFormModalLeInboundDeliveryCategory(ViewModelFormModalController):
	_name = "form.modal:le.inbound.delivery.category"
	_view_name = "le.inbound.delivery.category/form.modal"
	_description = "Category Inbound Delivery"

class ViewModelFormLeInboundDeliveryCategory(ViewModelFormController):
	_name = "form:le.inbound.delivery.category"
	_view_name = "le.inbound.delivery.category/form"
	_description = "Category Inbound Delivery"

class ViewModelTreeLeInboundDeliveryCategory(ViewModelTreeController):
	_name = "tree:le.inbound.delivery.category"
	_view_name = "le.inbound.delivery.category/tree"
	_description = "Category Inbound Delivery"
