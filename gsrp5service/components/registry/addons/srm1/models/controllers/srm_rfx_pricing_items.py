from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxPricingItems(ViewModelFindController):
	_name = "find:srm.rfx.pricing.items"
	_view_name = "srm.rfx.pricing.items/find"
	_description = "RFX Item Pricing"

class ViewModelO2MFormSrmRfxPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.pricing.items"
	_view_name = "srm.rfx.pricing.items/o2m-form"
	_description = "RFX Item Pricing"

class ViewModelO2MListSrmRfxPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.pricing.items"
	_view_name = "srm.rfx.pricing.items/o2m-list"
	_description = "RFX Item Pricing"
