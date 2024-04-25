from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmAuctionTypes(ViewModelSearchController):
	_name = "search:srm.auction.types"
	_view_name = "srm.auction.types/search"
	_description = "Types SRM Auction"

class ViewModelFindSrmAuctionTypes(ViewModelFindController):
	_name = "find:srm.auction.types"
	_view_name = "srm.auction.types/find"
	_description = "Types SRM Auction"

class ViewModelListSrmAuctionTypes(ViewModelListController):
	_name = "list:srm.auction.types"
	_view_name = "srm.auction.types/list"
	_description = "Types SRM Auction"

class ViewModelFormModalSrmAuctionTypes(ViewModelFormModalController):
	_name = "form.modal:srm.auction.types"
	_view_name = "srm.auction.types/form.modal"
	_description = "Types SRM Auction"

class ViewModelFormSrmAuctionTypes(ViewModelFormController):
	_name = "form:srm.auction.types"
	_view_name = "srm.auction.types/form"
	_description = "Types SRM Auction"
