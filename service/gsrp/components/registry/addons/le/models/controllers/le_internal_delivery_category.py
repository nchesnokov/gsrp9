from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchLeInternalDeliveryCategory(ViewModelSearchController):
	_name = "search:le.internal.delivery.category"
	_view_name = "le.internal.delivery.category/search"
	_description = "Category Internal Delivery"

class ViewModelFindLeInternalDeliveryCategory(ViewModelFindController):
	_name = "find:le.internal.delivery.category"
	_view_name = "le.internal.delivery.category/find"
	_description = "Category Internal Delivery"

class ViewModelListLeInternalDeliveryCategory(ViewModelListController):
	_name = "list:le.internal.delivery.category"
	_view_name = "le.internal.delivery.category/list"
	_description = "Category Internal Delivery"

class ViewModelFormModalLeInternalDeliveryCategory(ViewModelFormModalController):
	_name = "form.modal:le.internal.delivery.category"
	_view_name = "le.internal.delivery.category/form.modal"
	_description = "Category Internal Delivery"

class ViewModelFormLeInternalDeliveryCategory(ViewModelFormController):
	_name = "form:le.internal.delivery.category"
	_view_name = "le.internal.delivery.category/form"
	_description = "Category Internal Delivery"

class ViewModelTreeLeInternalDeliveryCategory(ViewModelTreeController):
	_name = "tree:le.internal.delivery.category"
	_view_name = "le.internal.delivery.category/tree"
	_description = "Category Internal Delivery"
