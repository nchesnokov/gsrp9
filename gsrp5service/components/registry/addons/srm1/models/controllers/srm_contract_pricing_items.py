from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractPricingItems(ViewModelFindController):
	_name = "find:srm.contract.pricing.items"
	_view_name = "srm.contract.pricing.items/find"
	_description = "Contract Item Pricing"

class ViewModelO2MFormSrmContractPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.pricing.items"
	_view_name = "srm.contract.pricing.items/o2m-form"
	_description = "Contract Item Pricing"

class ViewModelO2MListSrmContractPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.pricing.items"
	_view_name = "srm.contract.pricing.items/o2m-list"
	_description = "Contract Item Pricing"
