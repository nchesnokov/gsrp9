from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionItemTexts(ViewModelFindController):
	_name = "find:srm.auction.item.texts"
	_view_name = "srm.auction.item.texts/find"
	_description = "SRM Auction Item Texts"

class ViewModelO2MFormSrmAuctionItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.item.texts"
	_view_name = "srm.auction.item.texts/o2m-form"
	_description = "SRM Auction Item Texts"

class ViewModelO2MListSrmAuctionItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.item.texts"
	_view_name = "srm.auction.item.texts/o2m-list"
	_description = "SRM Auction Item Texts"
