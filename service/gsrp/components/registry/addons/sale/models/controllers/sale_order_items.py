from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderItems(ViewModelFindController):
	_name = "find:sale.order.items"
	_view_name = "sale.order.items/find"
	_description = "Sale Order Items"

class ViewModelO2MFormSaleOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.items"
	_view_name = "sale.order.items/o2m-form"
	_description = "Sale Order Items"

class ViewModelO2MListSaleOrderItems(ViewModelO2MListController):
	_name = "o2m-list:sale.order.items"
	_view_name = "sale.order.items/o2m-list"
	_description = "Sale Order Items"
