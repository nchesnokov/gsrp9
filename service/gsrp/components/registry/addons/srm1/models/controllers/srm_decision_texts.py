from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionTexts(ViewModelFindController):
	_name = "find:srm.decision.texts"
	_view_name = "srm.decision.texts/find"
	_description = "SRM Decision Texts"

class ViewModelO2MFormSrmDecisionTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.texts"
	_view_name = "srm.decision.texts/o2m-form"
	_description = "SRM Decision Texts"

class ViewModelO2MListSrmDecisionTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.texts"
	_view_name = "srm.decision.texts/o2m-list"
	_description = "SRM Decision Texts"
