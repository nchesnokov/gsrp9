from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderTypeItems(ViewModelFindController):
	_name = "find:purchase.order.type.items"
	_view_name = "purchase.order.type.items/find"
	_description = "Plates Of Purchase Order Items"

class ViewModelO2MFormPurchaseOrderTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.type.items"
	_view_name = "purchase.order.type.items/o2m-form"
	_description = "Plates Of Purchase Order Items"

class ViewModelO2MListPurchaseOrderTypeItems(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.type.items"
	_view_name = "purchase.order.type.items/o2m-list"
	_description = "Plates Of Purchase Order Items"
