from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderItemOutputPlates(ViewModelFindController):
	_name = "find:purchase.order.item.output.plates"
	_view_name = "purchase.order.item.output.plates/find"
	_description = "Purchase Order Item Output Plates"

class ViewModelO2MFormPurchaseOrderItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.item.output.plates"
	_view_name = "purchase.order.item.output.plates/o2m-form"
	_description = "Purchase Order Item Output Plates"

class ViewModelO2MKanbanPurchaseOrderItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:purchase.order.item.output.plates"
	_view_name = "purchase.order.item.output.plates/o2m-kanban"
	_description = "Purchase Order Item Output Plates"

class ViewModelO2MListPurchaseOrderItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.item.output.plates"
	_view_name = "purchase.order.item.output.plates/o2m-list"
	_description = "Purchase Order Item Output Plates"
