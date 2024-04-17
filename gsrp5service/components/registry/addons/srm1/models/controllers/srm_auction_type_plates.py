from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionTypePlates(ViewModelFindController):
	_name = "find:srm.auction.type.plates"
	_view_name = "srm.auction.type.plates/find"
	_description = "SRM Auction Plates"

class ViewModelO2MFormSrmAuctionTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.type.plates"
	_view_name = "srm.auction.type.plates/o2m-form"
	_description = "SRM Auction Plates"

class ViewModelO2MListSrmAuctionTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.type.plates"
	_view_name = "srm.auction.type.plates/o2m-list"
	_description = "SRM Auction Plates"
