from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionPricing(ViewModelFindController):
	_name = "find:srm.auction.pricing"
	_view_name = "srm.auction.pricing/find"
	_description = "SRM Auction Pricing"

class ViewModelO2MFormSrmAuctionPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.pricing"
	_view_name = "srm.auction.pricing/o2m-form"
	_description = "SRM Auction Pricing"

class ViewModelO2MListSrmAuctionPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.pricing"
	_view_name = "srm.auction.pricing/o2m-list"
	_description = "SRM Auction Pricing"
