from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionTypeRoles(ViewModelFindController):
	_name = "find:srm.auction.type.roles"
	_view_name = "srm.auction.type.roles/find"
	_description = "Role SRM Auction Types"

class ViewModelO2MFormSrmAuctionTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.type.roles"
	_view_name = "srm.auction.type.roles/o2m-form"
	_description = "Role SRM Auction Types"

class ViewModelO2MListSrmAuctionTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.type.roles"
	_view_name = "srm.auction.type.roles/o2m-list"
	_description = "Role SRM Auction Types"
