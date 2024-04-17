from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionTypeDeadlines(ViewModelFindController):
	_name = "find:srm.auction.type.deadlines"
	_view_name = "srm.auction.type.deadlines/find"
	_description = "Deadlines SRM Auction Types"

class ViewModelO2MFormSrmAuctionTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.type.deadlines"
	_view_name = "srm.auction.type.deadlines/o2m-form"
	_description = "Deadlines SRM Auction Types"

class ViewModelO2MListSrmAuctionTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.type.deadlines"
	_view_name = "srm.auction.type.deadlines/o2m-list"
	_description = "Deadlines SRM Auction Types"
