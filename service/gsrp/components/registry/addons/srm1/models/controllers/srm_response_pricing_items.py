from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponsePricingItems(ViewModelFindController):
	_name = "find:srm.response.pricing.items"
	_view_name = "srm.response.pricing.items/find"
	_description = "Response Item Pricing"

class ViewModelO2MFormSrmResponsePricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.pricing.items"
	_view_name = "srm.response.pricing.items/o2m-form"
	_description = "Response Item Pricing"

class ViewModelO2MListSrmResponsePricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.response.pricing.items"
	_view_name = "srm.response.pricing.items/o2m-list"
	_description = "Response Item Pricing"
