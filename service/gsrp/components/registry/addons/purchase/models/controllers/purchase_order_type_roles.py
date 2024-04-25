from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderTypeRoles(ViewModelFindController):
	_name = "find:purchase.order.type.roles"
	_view_name = "purchase.order.type.roles/find"
	_description = "Role Purchase Order Types"

class ViewModelO2MFormPurchaseOrderTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.type.roles"
	_view_name = "purchase.order.type.roles/o2m-form"
	_description = "Role Purchase Order Types"

class ViewModelO2MListPurchaseOrderTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.type.roles"
	_view_name = "purchase.order.type.roles/o2m-list"
	_description = "Role Purchase Order Types"
