from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferPricing(ViewModelFindController):
	_name = "find:srm.offer.pricing"
	_view_name = "srm.offer.pricing/find"
	_description = "SRM Offer Pricing"

class ViewModelO2MFormSrmOfferPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.pricing"
	_view_name = "srm.offer.pricing/o2m-form"
	_description = "SRM Offer Pricing"

class ViewModelO2MListSrmOfferPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.pricing"
	_view_name = "srm.offer.pricing/o2m-list"
	_description = "SRM Offer Pricing"
