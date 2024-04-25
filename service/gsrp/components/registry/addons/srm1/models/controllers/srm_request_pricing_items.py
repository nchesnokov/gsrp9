from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestPricingItems(ViewModelFindController):
	_name = "find:srm.request.pricing.items"
	_view_name = "srm.request.pricing.items/find"
	_description = "Request Item Pricing"

class ViewModelO2MFormSrmRequestPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.pricing.items"
	_view_name = "srm.request.pricing.items/o2m-form"
	_description = "Request Item Pricing"

class ViewModelO2MListSrmRequestPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.request.pricing.items"
	_view_name = "srm.request.pricing.items/o2m-list"
	_description = "Request Item Pricing"
