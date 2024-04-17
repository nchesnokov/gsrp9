from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSrmAuctionCategory(ViewModelSearchController):
	_name = "search:srm.auction.category"
	_view_name = "srm.auction.category/search"
	_description = "Category SRM Auction"

class ViewModelFindSrmAuctionCategory(ViewModelFindController):
	_name = "find:srm.auction.category"
	_view_name = "srm.auction.category/find"
	_description = "Category SRM Auction"

class ViewModelListSrmAuctionCategory(ViewModelListController):
	_name = "list:srm.auction.category"
	_view_name = "srm.auction.category/list"
	_description = "Category SRM Auction"

class ViewModelFormModalSrmAuctionCategory(ViewModelFormModalController):
	_name = "form.modal:srm.auction.category"
	_view_name = "srm.auction.category/form.modal"
	_description = "Category SRM Auction"

class ViewModelFormSrmAuctionCategory(ViewModelFormController):
	_name = "form:srm.auction.category"
	_view_name = "srm.auction.category/form"
	_description = "Category SRM Auction"

class ViewModelTreeSrmAuctionCategory(ViewModelTreeController):
	_name = "tree:srm.auction.category"
	_view_name = "srm.auction.category/tree"
	_description = "Category SRM Auction"
