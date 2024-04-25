from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindTmOrderItems(ViewModelFindController):
	_name = "find:tm.order.items"
	_view_name = "tm.order.items/find"
	_description = "Order Items"

class ViewModelO2MFormTmOrderItems(ViewModelO2MFormController):
	_name = "o2m-form:tm.order.items"
	_view_name = "tm.order.items/o2m-form"
	_description = "Order Items"

class ViewModelO2MListTmOrderItems(ViewModelO2MListController):
	_name = "o2m-list:tm.order.items"
	_view_name = "tm.order.items/o2m-list"
	_description = "Order Items"
