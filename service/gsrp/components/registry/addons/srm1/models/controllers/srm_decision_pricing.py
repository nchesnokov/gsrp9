from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionPricing(ViewModelFindController):
	_name = "find:srm.decision.pricing"
	_view_name = "srm.decision.pricing/find"
	_description = "SRM Decision Pricing"

class ViewModelO2MFormSrmDecisionPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.pricing"
	_view_name = "srm.decision.pricing/o2m-form"
	_description = "SRM Decision Pricing"

class ViewModelO2MListSrmDecisionPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.pricing"
	_view_name = "srm.decision.pricing/o2m-list"
	_description = "SRM Decision Pricing"
