from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionTypeItems(ViewModelFindController):
	_name = "find:srm.decision.type.items"
	_view_name = "srm.decision.type.items/find"
	_description = "Type of SRM Decision Items"

class ViewModelO2MFormSrmDecisionTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.type.items"
	_view_name = "srm.decision.type.items/o2m-form"
	_description = "Type of SRM Decision Items"

class ViewModelO2MListSrmDecisionTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.type.items"
	_view_name = "srm.decision.type.items/o2m-list"
	_description = "Type of SRM Decision Items"
