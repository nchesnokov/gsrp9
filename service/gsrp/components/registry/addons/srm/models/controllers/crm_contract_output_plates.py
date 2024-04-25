from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractOutputPlates(ViewModelFindController):
	_name = "find:crm.contract.output.plates"
	_view_name = "crm.contract.output.plates/find"
	_description = "Crm Contract Output Plates"

class ViewModelO2MFormCrmContractOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.output.plates"
	_view_name = "crm.contract.output.plates/o2m-form"
	_description = "Crm Contract Output Plates"

class ViewModelO2MKanbanCrmContractOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:crm.contract.output.plates"
	_view_name = "crm.contract.output.plates/o2m-kanban"
	_description = "Crm Contract Output Plates"

class ViewModelO2MListCrmContractOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.output.plates"
	_view_name = "crm.contract.output.plates/o2m-list"
	_description = "Crm Contract Output Plates"
