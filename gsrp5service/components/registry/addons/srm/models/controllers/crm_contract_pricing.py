from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractPricing(ViewModelFindController):
	_name = "find:crm.contract.pricing"
	_view_name = "crm.contract.pricing/find"
	_description = "Crm Contract Pricing"

class ViewModelO2MFormCrmContractPricing(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.pricing"
	_view_name = "crm.contract.pricing/o2m-form"
	_description = "Crm Contract Pricing"

class ViewModelO2MListCrmContractPricing(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.pricing"
	_view_name = "crm.contract.pricing/o2m-list"
	_description = "Crm Contract Pricing"
