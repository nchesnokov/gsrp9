from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderItemOutputPlates(ViewModelFindController):
	_name = "find:sale.order.item.output.plates"
	_view_name = "sale.order.item.output.plates/find"
	_description = "Sale Order Item Output Plates"

class ViewModelO2MFormSaleOrderItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.item.output.plates"
	_view_name = "sale.order.item.output.plates/o2m-form"
	_description = "Sale Order Item Output Plates"

class ViewModelO2MKanbanSaleOrderItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:sale.order.item.output.plates"
	_view_name = "sale.order.item.output.plates/o2m-kanban"
	_description = "Sale Order Item Output Plates"

class ViewModelO2MListSaleOrderItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:sale.order.item.output.plates"
	_view_name = "sale.order.item.output.plates/o2m-list"
	_description = "Sale Order Item Output Plates"
