from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRfxPricing(ViewModelFindController):
	_name = "find:srm.rfx.pricing"
	_view_name = "srm.rfx.pricing/find"
	_description = "SRM RFX Pricing"

class ViewModelO2MFormSrmRfxPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.rfx.pricing"
	_view_name = "srm.rfx.pricing/o2m-form"
	_description = "SRM RFX Pricing"

class ViewModelO2MListSrmRfxPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.rfx.pricing"
	_view_name = "srm.rfx.pricing/o2m-list"
	_description = "SRM RFX Pricing"
