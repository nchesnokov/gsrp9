from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionTypePlates(ViewModelFindController):
	_name = "find:srm.decision.type.plates"
	_view_name = "srm.decision.type.plates/find"
	_description = "SRM Decision Plates"

class ViewModelO2MFormSrmDecisionTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.type.plates"
	_view_name = "srm.decision.type.plates/o2m-form"
	_description = "SRM Decision Plates"

class ViewModelO2MListSrmDecisionTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.type.plates"
	_view_name = "srm.decision.type.plates/o2m-list"
	_description = "SRM Decision Plates"
