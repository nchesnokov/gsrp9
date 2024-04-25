from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractOutputPlates(ViewModelFindController):
	_name = "find:srm.contract.output.plates"
	_view_name = "srm.contract.output.plates/find"
	_description = "SRM Contract Output Plates"

class ViewModelO2MFormSrmContractOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.output.plates"
	_view_name = "srm.contract.output.plates/o2m-form"
	_description = "SRM Contract Output Plates"

class ViewModelO2MKanbanSrmContractOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.contract.output.plates"
	_view_name = "srm.contract.output.plates/o2m-kanban"
	_description = "SRM Contract Output Plates"

class ViewModelO2MListSrmContractOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.output.plates"
	_view_name = "srm.contract.output.plates/o2m-list"
	_description = "SRM Contract Output Plates"
