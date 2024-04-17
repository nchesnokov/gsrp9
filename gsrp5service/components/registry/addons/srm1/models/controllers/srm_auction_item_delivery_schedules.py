from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MCalendarController
from gsrp5service.obj.controller.controller import ViewModelO2MGraphController
from gsrp5service.obj.controller.controller import ViewModelO2MMdxController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionItemDeliverySchedules(ViewModelFindController):
	_name = "find:srm.auction.item.delivery.schedules"
	_view_name = "srm.auction.item.delivery.schedules/find"
	_description = "SRM Auction Delivery Schedules"

class ViewModelO2MFormSrmAuctionItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.item.delivery.schedules"
	_view_name = "srm.auction.item.delivery.schedules/o2m-form"
	_description = "SRM Auction Delivery Schedules"

class ViewModelO2MCalendarSrmAuctionItemDeliverySchedules(ViewModelO2MCalendarController):
	_name = "o2m-calendar:srm.auction.item.delivery.schedules"
	_view_name = "srm.auction.item.delivery.schedules/o2m-calendar"
	_description = "SRM Auction Delivery Schedules"

class ViewModelO2MGraphSrmAuctionItemDeliverySchedules(ViewModelO2MGraphController):
	_name = "o2m-graph:srm.auction.item.delivery.schedules"
	_view_name = "srm.auction.item.delivery.schedules/o2m-graph"
	_description = "SRM Auction Delivery Schedules"

class ViewModelO2MMdxSrmAuctionItemDeliverySchedules(ViewModelO2MMdxController):
	_name = "o2m-mdx:srm.auction.item.delivery.schedules"
	_view_name = "srm.auction.item.delivery.schedules/o2m-mdx"
	_description = "SRM Auction Delivery Schedules"

class ViewModelO2MListSrmAuctionItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.item.delivery.schedules"
	_view_name = "srm.auction.item.delivery.schedules/o2m-list"
	_description = "SRM Auction Delivery Schedules"
