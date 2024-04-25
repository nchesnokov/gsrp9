from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindEhsDisassemblyOrderDeliverySchedules(ViewModelFindController):
	_name = "find:ehs.disassembly.order.delivery.schedules"
	_view_name = "ehs.disassembly.order.delivery.schedules/find"
	_description = "Disassembly Order Delivery Schedule"

class ViewModelO2MFormEhsDisassemblyOrderDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:ehs.disassembly.order.delivery.schedules"
	_view_name = "ehs.disassembly.order.delivery.schedules/o2m-form"
	_description = "Disassembly Order Delivery Schedule"

class ViewModelO2MListEhsDisassemblyOrderDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:ehs.disassembly.order.delivery.schedules"
	_view_name = "ehs.disassembly.order.delivery.schedules/o2m-list"
	_description = "Disassembly Order Delivery Schedule"
