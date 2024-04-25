from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionItemRoles(ViewModelFindController):
	_name = "find:srm.auction.item.roles"
	_view_name = "srm.auction.item.roles/find"
	_description = "SRM Auction Roles"

class ViewModelO2MFormSrmAuctionItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.item.roles"
	_view_name = "srm.auction.item.roles/o2m-form"
	_description = "SRM Auction Roles"

class ViewModelO2MListSrmAuctionItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.item.roles"
	_view_name = "srm.auction.item.roles/o2m-list"
	_description = "SRM Auction Roles"
