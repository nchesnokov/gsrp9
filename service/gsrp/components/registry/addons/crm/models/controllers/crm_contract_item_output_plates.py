from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractItemOutputPlates(ViewModelFindController):
	_name = "find:crm.contract.item.output.plates"
	_view_name = "crm.contract.item.output.plates/find"
	_description = "Crm Contract Item Output Plates"

class ViewModelO2MFormCrmContractItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.item.output.plates"
	_view_name = "crm.contract.item.output.plates/o2m-form"
	_description = "Crm Contract Item Output Plates"

class ViewModelO2MKanbanCrmContractItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:crm.contract.item.output.plates"
	_view_name = "crm.contract.item.output.plates/o2m-kanban"
	_description = "Crm Contract Item Output Plates"

class ViewModelO2MListCrmContractItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.item.output.plates"
	_view_name = "crm.contract.item.output.plates/o2m-list"
	_description = "Crm Contract Item Output Plates"
