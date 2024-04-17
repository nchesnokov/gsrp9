from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandPricing(ViewModelFindController):
	_name = "find:srm.demand.pricing"
	_view_name = "srm.demand.pricing/find"
	_description = "SRM Demand Pricing"

class ViewModelO2MFormSrmDemandPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.pricing"
	_view_name = "srm.demand.pricing/o2m-form"
	_description = "SRM Demand Pricing"

class ViewModelO2MListSrmDemandPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.pricing"
	_view_name = "srm.demand.pricing/o2m-list"
	_description = "SRM Demand Pricing"
