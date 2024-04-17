from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchLeOutboundDeliveryCategory(ViewModelSearchController):
	_name = "search:le.outbound.delivery.category"
	_view_name = "le.outbound.delivery.category/search"
	_description = "Category Outbound Delivery"

class ViewModelFindLeOutboundDeliveryCategory(ViewModelFindController):
	_name = "find:le.outbound.delivery.category"
	_view_name = "le.outbound.delivery.category/find"
	_description = "Category Outbound Delivery"

class ViewModelListLeOutboundDeliveryCategory(ViewModelListController):
	_name = "list:le.outbound.delivery.category"
	_view_name = "le.outbound.delivery.category/list"
	_description = "Category Outbound Delivery"

class ViewModelFormModalLeOutboundDeliveryCategory(ViewModelFormModalController):
	_name = "form.modal:le.outbound.delivery.category"
	_view_name = "le.outbound.delivery.category/form.modal"
	_description = "Category Outbound Delivery"

class ViewModelFormLeOutboundDeliveryCategory(ViewModelFormController):
	_name = "form:le.outbound.delivery.category"
	_view_name = "le.outbound.delivery.category/form"
	_description = "Category Outbound Delivery"

class ViewModelTreeLeOutboundDeliveryCategory(ViewModelTreeController):
	_name = "tree:le.outbound.delivery.category"
	_view_name = "le.outbound.delivery.category/tree"
	_description = "Category Outbound Delivery"
