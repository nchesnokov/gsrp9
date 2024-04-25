from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderOutputPlates(ViewModelFindController):
	_name = "find:sale.order.output.plates"
	_view_name = "sale.order.output.plates/find"
	_description = "Sale Order Output Plates"

class ViewModelO2MFormSaleOrderOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.output.plates"
	_view_name = "sale.order.output.plates/o2m-form"
	_description = "Sale Order Output Plates"

class ViewModelO2MKanbanSaleOrderOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:sale.order.output.plates"
	_view_name = "sale.order.output.plates/o2m-kanban"
	_description = "Sale Order Output Plates"

class ViewModelO2MListSaleOrderOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:sale.order.output.plates"
	_view_name = "sale.order.output.plates/o2m-list"
	_description = "Sale Order Output Plates"
