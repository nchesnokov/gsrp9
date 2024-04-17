from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionItems(ViewModelFindController):
	_name = "find:srm.auction.items"
	_view_name = "srm.auction.items/find"
	_description = "SRM Auction Item"

class ViewModelO2MFormSrmAuctionItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.items"
	_view_name = "srm.auction.items/o2m-form"
	_description = "SRM Auction Item"

class ViewModelO2MListSrmAuctionItems(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.items"
	_view_name = "srm.auction.items/o2m-list"
	_description = "SRM Auction Item"
