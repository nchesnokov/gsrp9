from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanPricingItems(ViewModelFindController):
	_name = "find:srm.plan.pricing.items"
	_view_name = "srm.plan.pricing.items/find"
	_description = "Plan Item Pricing"

class ViewModelO2MFormSrmPlanPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.pricing.items"
	_view_name = "srm.plan.pricing.items/o2m-form"
	_description = "Plan Item Pricing"

class ViewModelO2MListSrmPlanPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.pricing.items"
	_view_name = "srm.plan.pricing.items/o2m-list"
	_description = "Plan Item Pricing"
