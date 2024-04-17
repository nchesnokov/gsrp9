from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionItemOutputPlates(ViewModelFindController):
	_name = "find:srm.decision.item.output.plates"
	_view_name = "srm.decision.item.output.plates/find"
	_description = "Decision Item Output Plates"

class ViewModelO2MFormSrmDecisionItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.item.output.plates"
	_view_name = "srm.decision.item.output.plates/o2m-form"
	_description = "Decision Item Output Plates"

class ViewModelO2MKanbanSrmDecisionItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.decision.item.output.plates"
	_view_name = "srm.decision.item.output.plates/o2m-kanban"
	_description = "Decision Item Output Plates"

class ViewModelO2MListSrmDecisionItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.item.output.plates"
	_view_name = "srm.decision.item.output.plates/o2m-list"
	_description = "Decision Item Output Plates"
