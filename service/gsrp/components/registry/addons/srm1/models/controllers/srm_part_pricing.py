from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartPricing(ViewModelFindController):
	_name = "find:srm.part.pricing"
	_view_name = "srm.part.pricing/find"
	_description = "SRM Part Pricing"

class ViewModelO2MFormSrmPartPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.pricing"
	_view_name = "srm.part.pricing/o2m-form"
	_description = "SRM Part Pricing"

class ViewModelO2MListSrmPartPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.part.pricing"
	_view_name = "srm.part.pricing/o2m-list"
	_description = "SRM Part Pricing"
