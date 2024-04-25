from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderRoles(ViewModelFindController):
	_name = "find:purchase.order.roles"
	_view_name = "purchase.order.roles/find"
	_description = "Purchase Order Roles"

class ViewModelO2MFormPurchaseOrderRoles(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.roles"
	_view_name = "purchase.order.roles/o2m-form"
	_description = "Purchase Order Roles"

class ViewModelO2MListPurchaseOrderRoles(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.roles"
	_view_name = "purchase.order.roles/o2m-list"
	_description = "Purchase Order Roles"
