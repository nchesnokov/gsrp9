from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderItemRoles(ViewModelFindController):
	_name = "find:purchase.order.item.roles"
	_view_name = "purchase.order.item.roles/find"
	_description = "Purchase Order Roles"

class ViewModelO2MFormPurchaseOrderItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.item.roles"
	_view_name = "purchase.order.item.roles/o2m-form"
	_description = "Purchase Order Roles"

class ViewModelO2MListPurchaseOrderItemRoles(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.item.roles"
	_view_name = "purchase.order.item.roles/o2m-list"
	_description = "Purchase Order Roles"
