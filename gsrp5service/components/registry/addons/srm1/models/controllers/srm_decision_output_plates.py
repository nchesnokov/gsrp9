from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionOutputPlates(ViewModelFindController):
	_name = "find:srm.decision.output.plates"
	_view_name = "srm.decision.output.plates/find"
	_description = "SRM Decision Output Plates"

class ViewModelO2MFormSrmDecisionOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.output.plates"
	_view_name = "srm.decision.output.plates/o2m-form"
	_description = "SRM Decision Output Plates"

class ViewModelO2MKanbanSrmDecisionOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.decision.output.plates"
	_view_name = "srm.decision.output.plates/o2m-kanban"
	_description = "SRM Decision Output Plates"

class ViewModelO2MListSrmDecisionOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.output.plates"
	_view_name = "srm.decision.output.plates/o2m-list"
	_description = "SRM Decision Output Plates"
