from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionPaymentSchedules(ViewModelFindController):
	_name = "find:srm.auction.payment.schedules"
	_view_name = "srm.auction.payment.schedules/find"
	_description = "SRM Auction Payment Schedules"

class ViewModelO2MFormSrmAuctionPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.payment.schedules"
	_view_name = "srm.auction.payment.schedules/o2m-form"
	_description = "SRM Auction Payment Schedules"

class ViewModelO2MListSrmAuctionPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.payment.schedules"
	_view_name = "srm.auction.payment.schedules/o2m-list"
	_description = "SRM Auction Payment Schedules"
