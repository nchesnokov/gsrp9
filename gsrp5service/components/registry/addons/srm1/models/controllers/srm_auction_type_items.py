from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionTypeItems(ViewModelFindController):
	_name = "find:srm.auction.type.items"
	_view_name = "srm.auction.type.items/find"
	_description = "Type of SRM Auction Items"

class ViewModelO2MFormSrmAuctionTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.type.items"
	_view_name = "srm.auction.type.items/o2m-form"
	_description = "Type of SRM Auction Items"

class ViewModelO2MListSrmAuctionTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.type.items"
	_view_name = "srm.auction.type.items/o2m-list"
	_description = "Type of SRM Auction Items"
