from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractPricing(ViewModelFindController):
	_name = "find:srm.contract.pricing"
	_view_name = "srm.contract.pricing/find"
	_description = "SRM Contract Pricing"

class ViewModelO2MFormSrmContractPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.pricing"
	_view_name = "srm.contract.pricing/o2m-form"
	_description = "SRM Contract Pricing"

class ViewModelO2MListSrmContractPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.pricing"
	_view_name = "srm.contract.pricing/o2m-list"
	_description = "SRM Contract Pricing"
