from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionItemTexts(ViewModelFindController):
	_name = "find:srm.decision.item.texts"
	_view_name = "srm.decision.item.texts/find"
	_description = "SRM Decision Item Texts"

class ViewModelO2MFormSrmDecisionItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.item.texts"
	_view_name = "srm.decision.item.texts/o2m-form"
	_description = "SRM Decision Item Texts"

class ViewModelO2MListSrmDecisionItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.item.texts"
	_view_name = "srm.decision.item.texts/o2m-list"
	_description = "SRM Decision Item Texts"
