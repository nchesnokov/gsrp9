from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderSchedules(ViewModelFindController):
	_name = "find:mm.disassembly.order.schedules"
	_view_name = "mm.disassembly.order.schedules/find"
	_description = "Disassembly Order Delivery Schedule"

class ViewModelO2MFormMmDisassemblyOrderSchedules(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.schedules"
	_view_name = "mm.disassembly.order.schedules/o2m-form"
	_description = "Disassembly Order Delivery Schedule"

class ViewModelO2MListMmDisassemblyOrderSchedules(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.schedules"
	_view_name = "mm.disassembly.order.schedules/o2m-list"
	_description = "Disassembly Order Delivery Schedule"
