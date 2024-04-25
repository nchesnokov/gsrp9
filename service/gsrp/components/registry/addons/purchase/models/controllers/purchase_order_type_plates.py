from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderTypePlates(ViewModelFindController):
	_name = "find:purchase.order.type.plates"
	_view_name = "purchase.order.type.plates/find"
	_description = "Purchase Order Plates"

class ViewModelO2MFormPurchaseOrderTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.type.plates"
	_view_name = "purchase.order.type.plates/o2m-form"
	_description = "Purchase Order Plates"

class ViewModelO2MListPurchaseOrderTypePlates(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.type.plates"
	_view_name = "purchase.order.type.plates/o2m-list"
	_description = "Purchase Order Plates"
