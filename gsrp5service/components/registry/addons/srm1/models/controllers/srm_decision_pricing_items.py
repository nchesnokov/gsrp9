from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDecisionPricingItems(ViewModelFindController):
	_name = "find:srm.decision.pricing.items"
	_view_name = "srm.decision.pricing.items/find"
	_description = "Decision Item Pricing"

class ViewModelO2MFormSrmDecisionPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.decision.pricing.items"
	_view_name = "srm.decision.pricing.items/o2m-form"
	_description = "Decision Item Pricing"

class ViewModelO2MListSrmDecisionPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.decision.pricing.items"
	_view_name = "srm.decision.pricing.items/o2m-list"
	_description = "Decision Item Pricing"
