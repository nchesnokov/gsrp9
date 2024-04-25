from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderTypeItems(ViewModelFindController):
	_name = "find:sale.order.type.items"
	_view_name = "sale.order.type.items/find"
	_description = "Role Sale Order Items"

class ViewModelO2MFormSaleOrderTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.type.items"
	_view_name = "sale.order.type.items/o2m-form"
	_description = "Role Sale Order Items"

class ViewModelO2MListSaleOrderTypeItems(ViewModelO2MListController):
	_name = "o2m-list:sale.order.type.items"
	_view_name = "sale.order.type.items/o2m-list"
	_description = "Role Sale Order Items"
