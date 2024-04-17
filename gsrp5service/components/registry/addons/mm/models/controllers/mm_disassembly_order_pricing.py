from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderPricing(ViewModelFindController):
	_name = "find:mm.disassembly.order.pricing"
	_view_name = "mm.disassembly.order.pricing/find"
	_description = "Disassembly Order Pricing"

class ViewModelO2MFormMmDisassemblyOrderPricing(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.pricing"
	_view_name = "mm.disassembly.order.pricing/o2m-form"
	_description = "Disassembly Order Pricing"

class ViewModelO2MListMmDisassemblyOrderPricing(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.pricing"
	_view_name = "mm.disassembly.order.pricing/o2m-list"
	_description = "Disassembly Order Pricing"
