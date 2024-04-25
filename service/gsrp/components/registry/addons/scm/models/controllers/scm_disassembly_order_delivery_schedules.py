from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindScmDisassemblyOrderDeliverySchedules(ViewModelFindController):
	_name = "find:scm.disassembly.order.delivery.schedules"
	_view_name = "scm.disassembly.order.delivery.schedules/find"
	_description = "Disassembly Order Delivery Schedule"

class ViewModelO2MFormScmDisassemblyOrderDeliverySchedules(ViewModelO2MFormController):
	_name = "o2m-form:scm.disassembly.order.delivery.schedules"
	_view_name = "scm.disassembly.order.delivery.schedules/o2m-form"
	_description = "Disassembly Order Delivery Schedule"

class ViewModelO2MListScmDisassemblyOrderDeliverySchedules(ViewModelO2MListController):
	_name = "o2m-list:scm.disassembly.order.delivery.schedules"
	_view_name = "scm.disassembly.order.delivery.schedules/o2m-list"
	_description = "Disassembly Order Delivery Schedule"
