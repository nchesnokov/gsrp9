from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderTypeRoles(ViewModelFindController):
	_name = "find:sale.order.type.roles"
	_view_name = "sale.order.type.roles/find"
	_description = "Role Sale Order Types"

class ViewModelO2MFormSaleOrderTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.type.roles"
	_view_name = "sale.order.type.roles/o2m-form"
	_description = "Role Sale Order Types"

class ViewModelO2MListSaleOrderTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:sale.order.type.roles"
	_view_name = "sale.order.type.roles/o2m-list"
	_description = "Role Sale Order Types"
