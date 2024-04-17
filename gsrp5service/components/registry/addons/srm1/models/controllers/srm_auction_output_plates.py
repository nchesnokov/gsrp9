from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionOutputPlates(ViewModelFindController):
	_name = "find:srm.auction.output.plates"
	_view_name = "srm.auction.output.plates/find"
	_description = "SRM Auction Output Plates"

class ViewModelO2MFormSrmAuctionOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.output.plates"
	_view_name = "srm.auction.output.plates/o2m-form"
	_description = "SRM Auction Output Plates"

class ViewModelO2MKanbanSrmAuctionOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.auction.output.plates"
	_view_name = "srm.auction.output.plates/o2m-kanban"
	_description = "SRM Auction Output Plates"

class ViewModelO2MListSrmAuctionOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.output.plates"
	_view_name = "srm.auction.output.plates/o2m-list"
	_description = "SRM Auction Output Plates"
