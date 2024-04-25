from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanPricing(ViewModelFindController):
	_name = "find:srm.plan.pricing"
	_view_name = "srm.plan.pricing/find"
	_description = "SRM Plan Pricing"

class ViewModelO2MFormSrmPlanPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.pricing"
	_view_name = "srm.plan.pricing/o2m-form"
	_description = "SRM Plan Pricing"

class ViewModelO2MListSrmPlanPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.pricing"
	_view_name = "srm.plan.pricing/o2m-list"
	_description = "SRM Plan Pricing"
