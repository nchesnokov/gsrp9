from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartPricingItems(ViewModelFindController):
	_name = "find:srm.part.pricing.items"
	_view_name = "srm.part.pricing.items/find"
	_description = "Part Item Pricing"

class ViewModelO2MFormSrmPartPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.pricing.items"
	_view_name = "srm.part.pricing.items/o2m-form"
	_description = "Part Item Pricing"

class ViewModelO2MListSrmPartPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.part.pricing.items"
	_view_name = "srm.part.pricing.items/o2m-list"
	_description = "Part Item Pricing"
