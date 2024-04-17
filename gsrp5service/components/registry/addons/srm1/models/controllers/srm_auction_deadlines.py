from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MGanttController
from gsrp5service.obj.controller.controller import ViewModelO2MScheduleController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmAuctionDeadlines(ViewModelFindController):
	_name = "find:srm.auction.deadlines"
	_view_name = "srm.auction.deadlines/find"
	_description = "SRM Auction Deadlines"

class ViewModelO2MFormSrmAuctionDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.auction.deadlines"
	_view_name = "srm.auction.deadlines/o2m-form"
	_description = "SRM Auction Deadlines"

class ViewModelO2MGanttSrmAuctionDeadlines(ViewModelO2MGanttController):
	_name = "o2m-gantt:srm.auction.deadlines"
	_view_name = "srm.auction.deadlines/o2m-gantt"
	_description = "SRM Auction Deadlines"

class ViewModelO2MScheduleSrmAuctionDeadlines(ViewModelO2MScheduleController):
	_name = "o2m-schedule:srm.auction.deadlines"
	_view_name = "srm.auction.deadlines/o2m-schedule"
	_description = "SRM Auction Deadlines"

class ViewModelO2MListSrmAuctionDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.auction.deadlines"
	_view_name = "srm.auction.deadlines/o2m-list"
	_description = "SRM Auction Deadlines"
