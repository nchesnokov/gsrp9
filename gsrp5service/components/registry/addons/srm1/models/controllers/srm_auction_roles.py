from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionRoles(ViewModelFindController):
	_name = "find:srm.auction.roles"
	_view_name = "srm.auction.roles/find"
	_description = "SRM Auction Roles"

class ViewModelO2MFormSrmAuctionRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.roles"
	_view_name = "srm.auction.roles/o2m-form"
	_description = "SRM Auction Roles"

class ViewModelO2MListSrmAuctionRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.roles"
	_view_name = "srm.auction.roles/o2m-list"
	_description = "SRM Auction Roles"
