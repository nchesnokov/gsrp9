from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractPricingItems(ViewModelFindController):
	_name = "find:crm.contract.pricing.items"
	_view_name = "crm.contract.pricing.items/find"
	_description = "Crm Contract Item Pricing"

class ViewModelO2MFormCrmContractPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.pricing.items"
	_view_name = "crm.contract.pricing.items/o2m-form"
	_description = "Crm Contract Item Pricing"

class ViewModelO2MListCrmContractPricingItems(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.pricing.items"
	_view_name = "crm.contract.pricing.items/o2m-list"
	_description = "Crm Contract Item Pricing"
