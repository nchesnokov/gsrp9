from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.auction.item.payment.schedules"
	_view_name = "srm.auction.item.payment.schedules/find"
	_description = "Auction Item Payment Schedules"

class ViewModelO2MFormSrmAuctionItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.item.payment.schedules"
	_view_name = "srm.auction.item.payment.schedules/o2m-form"
	_description = "Auction Item Payment Schedules"

class ViewModelO2MListSrmAuctionItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.item.payment.schedules"
	_view_name = "srm.auction.item.payment.schedules/o2m-list"
	_description = "Auction Item Payment Schedules"
