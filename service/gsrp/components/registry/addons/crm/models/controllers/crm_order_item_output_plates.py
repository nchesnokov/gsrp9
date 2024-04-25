from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderItemOutputPlates(ViewModelFindController):
	_name = "find:crm.order.item.output.plates"
	_view_name = "crm.order.item.output.plates/find"
	_description = "CRM Order Item Output Plates"

class ViewModelO2MFormCrmOrderItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.item.output.plates"
	_view_name = "crm.order.item.output.plates/o2m-form"
	_description = "CRM Order Item Output Plates"

class ViewModelO2MKanbanCrmOrderItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:crm.order.item.output.plates"
	_view_name = "crm.order.item.output.plates/o2m-kanban"
	_description = "CRM Order Item Output Plates"

class ViewModelO2MListCrmOrderItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:crm.order.item.output.plates"
	_view_name = "crm.order.item.output.plates/o2m-list"
	_description = "CRM Order Item Output Plates"
