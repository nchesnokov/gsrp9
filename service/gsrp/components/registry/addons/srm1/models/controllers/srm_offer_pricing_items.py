from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmOfferPricingItems(ViewModelFindController):
	_name = "find:srm.offer.pricing.items"
	_view_name = "srm.offer.pricing.items/find"
	_description = "Offer Item Pricing"

class ViewModelO2MFormSrmOfferPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.offer.pricing.items"
	_view_name = "srm.offer.pricing.items/o2m-form"
	_description = "Offer Item Pricing"

class ViewModelO2MListSrmOfferPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.offer.pricing.items"
	_view_name = "srm.offer.pricing.items/o2m-list"
	_description = "Offer Item Pricing"
