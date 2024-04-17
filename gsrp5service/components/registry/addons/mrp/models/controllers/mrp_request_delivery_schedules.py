from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestDeliverySchedules(ViewModelFindController):
	_name = "find:mrp.request.delivery.schedules"
	_view_name = "mrp.request.delivery.schedules/find"
	_description = "MRP Request Delivery Schedule"

class ViewModelO2MFormMrpRequestDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.delivery.schedules"
	_view_name = "mrp.request.delivery.schedules/o2m-form"
	_description = "MRP Request Delivery Schedule"

class ViewModelO2MListMrpRequestDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.delivery.schedules"
	_view_name = "mrp.request.delivery.schedules/o2m-list"
	_description = "MRP Request Delivery Schedule"
