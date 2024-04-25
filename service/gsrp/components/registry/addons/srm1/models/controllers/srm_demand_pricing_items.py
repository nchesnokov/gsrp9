from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandPricingItems(ViewModelFindController):
	_name = "find:srm.demand.pricing.items"
	_view_name = "srm.demand.pricing.items/find"
	_description = "Demand Item Pricing"

class ViewModelO2MFormSrmDemandPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.pricing.items"
	_view_name = "srm.demand.pricing.items/o2m-form"
	_description = "Demand Item Pricing"

class ViewModelO2MListSrmDemandPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.pricing.items"
	_view_name = "srm.demand.pricing.items/o2m-list"
	_description = "Demand Item Pricing"
