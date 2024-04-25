from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionTexts(ViewModelFindController):
	_name = "find:srm.auction.texts"
	_view_name = "srm.auction.texts/find"
	_description = "SRM Auction Texts"

class ViewModelO2MFormSrmAuctionTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.texts"
	_view_name = "srm.auction.texts/o2m-form"
	_description = "SRM Auction Texts"

class ViewModelO2MListSrmAuctionTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.texts"
	_view_name = "srm.auction.texts/o2m-list"
	_description = "SRM Auction Texts"
