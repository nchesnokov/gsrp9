from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderOutputPlates(ViewModelFindController):
	_name = "find:crm.order.output.plates"
	_view_name = "crm.order.output.plates/find"
	_description = "CRM Order Output Plates"

class ViewModelO2MFormCrmOrderOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.output.plates"
	_view_name = "crm.order.output.plates/o2m-form"
	_description = "CRM Order Output Plates"

class ViewModelO2MKanbanCrmOrderOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:crm.order.output.plates"
	_view_name = "crm.order.output.plates/o2m-kanban"
	_description = "CRM Order Output Plates"

class ViewModelO2MListCrmOrderOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:crm.order.output.plates"
	_view_name = "crm.order.output.plates/o2m-list"
	_description = "CRM Order Output Plates"
