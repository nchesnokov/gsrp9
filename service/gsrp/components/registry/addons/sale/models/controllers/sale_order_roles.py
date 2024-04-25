from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderRoles(ViewModelFindController):
	_name = "find:sale.order.roles"
	_view_name = "sale.order.roles/find"
	_description = "Sale Order Roles"

class ViewModelO2MFormSaleOrderRoles(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.roles"
	_view_name = "sale.order.roles/o2m-form"
	_description = "Sale Order Roles"

class ViewModelO2MListSaleOrderRoles(ViewModelO2MListController):
	_name = "o2m-list:sale.order.roles"
	_view_name = "sale.order.roles/o2m-list"
	_description = "Sale Order Roles"
