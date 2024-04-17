from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmRequestItemDeliverySchedules(ViewModelFindController):
	_name = "find:ctrm.request.item.delivery.schedules"
	_view_name = "ctrm.request.item.delivery.schedules/find"
	_description = "CTRM REquest Item Delivery Schedules"

class ViewModelO2MFormCtrmRequestItemDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.request.item.delivery.schedules"
	_view_name = "ctrm.request.item.delivery.schedules/o2m-form"
	_description = "CTRM REquest Item Delivery Schedules"

class ViewModelO2MListCtrmRequestItemDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:ctrm.request.item.delivery.schedules"
	_view_name = "ctrm.request.item.delivery.schedules/o2m-list"
	_description = "CTRM REquest Item Delivery Schedules"
