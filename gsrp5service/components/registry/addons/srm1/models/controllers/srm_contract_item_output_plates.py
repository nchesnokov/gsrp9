from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractItemOutputPlates(ViewModelFindController):
	_name = "find:srm.contract.item.output.plates"
	_view_name = "srm.contract.item.output.plates/find"
	_description = "Contract Item Output Plates"

class ViewModelO2MFormSrmContractItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.item.output.plates"
	_view_name = "srm.contract.item.output.plates/o2m-form"
	_description = "Contract Item Output Plates"

class ViewModelO2MKanbanSrmContractItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.contract.item.output.plates"
	_view_name = "srm.contract.item.output.plates/o2m-kanban"
	_description = "Contract Item Output Plates"

class ViewModelO2MListSrmContractItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.item.output.plates"
	_view_name = "srm.contract.item.output.plates/o2m-list"
	_description = "Contract Item Output Plates"
