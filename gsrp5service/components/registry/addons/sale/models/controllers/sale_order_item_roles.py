from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderItemRoles(ViewModelFindController):
	_name = "find:sale.order.item.roles"
	_view_name = "sale.order.item.roles/find"
	_description = "Sale Order Roles"

class ViewModelO2MFormSaleOrderItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.item.roles"
	_view_name = "sale.order.item.roles/o2m-form"
	_description = "Sale Order Roles"

class ViewModelO2MListSaleOrderItemRoles(ViewModelO2MListController):
	_name = "o2m-list:sale.order.item.roles"
	_view_name = "sale.order.item.roles/o2m-list"
	_description = "Sale Order Roles"
