from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderOutputPlates(ViewModelFindController):
	_name = "find:purchase.order.output.plates"
	_view_name = "purchase.order.output.plates/find"
	_description = "Purchase Order Output Plates"

class ViewModelO2MFormPurchaseOrderOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.output.plates"
	_view_name = "purchase.order.output.plates/o2m-form"
	_description = "Purchase Order Output Plates"

class ViewModelO2MKanbanPurchaseOrderOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:purchase.order.output.plates"
	_view_name = "purchase.order.output.plates/o2m-kanban"
	_description = "Purchase Order Output Plates"

class ViewModelO2MListPurchaseOrderOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.output.plates"
	_view_name = "purchase.order.output.plates/o2m-list"
	_description = "Purchase Order Output Plates"
