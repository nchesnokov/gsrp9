from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionItemOutputPlates(ViewModelFindController):
	_name = "find:srm.auction.item.output.plates"
	_view_name = "srm.auction.item.output.plates/find"
	_description = "Auction Item Output Plates"

class ViewModelO2MFormSrmAuctionItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.item.output.plates"
	_view_name = "srm.auction.item.output.plates/o2m-form"
	_description = "Auction Item Output Plates"

class ViewModelO2MKanbanSrmAuctionItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.auction.item.output.plates"
	_view_name = "srm.auction.item.output.plates/o2m-kanban"
	_description = "Auction Item Output Plates"

class ViewModelO2MListSrmAuctionItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.item.output.plates"
	_view_name = "srm.auction.item.output.plates/o2m-list"
	_description = "Auction Item Output Plates"
