from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionPricingItems(ViewModelFindController):
	_name = "find:srm.auction.pricing.items"
	_view_name = "srm.auction.pricing.items/find"
	_description = "Auction Item Pricing"

class ViewModelO2MFormSrmAuctionPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.pricing.items"
	_view_name = "srm.auction.pricing.items/o2m-form"
	_description = "Auction Item Pricing"

class ViewModelO2MListSrmAuctionPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.pricing.items"
	_view_name = "srm.auction.pricing.items/o2m-list"
	_description = "Auction Item Pricing"
