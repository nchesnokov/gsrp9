from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderItems(ViewModelFindController):
	_name = "find:purchase.order.items"
	_view_name = "purchase.order.items/find"
	_description = "Purchase Order Items"

class ViewModelO2MFormPurchaseOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.items"
	_view_name = "purchase.order.items/o2m-form"
	_description = "Purchase Order Items"

class ViewModelO2MListPurchaseOrderItems(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.items"
	_view_name = "purchase.order.items/o2m-list"
	_description = "Purchase Order Items"
