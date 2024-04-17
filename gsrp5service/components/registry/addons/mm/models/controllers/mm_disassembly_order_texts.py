from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderTexts(ViewModelFindController):
	_name = "find:mm.disassembly.order.texts"
	_view_name = "mm.disassembly.order.texts/find"
	_description = "Disassembly Order Texts"

class ViewModelO2MFormMmDisassemblyOrderTexts(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.texts"
	_view_name = "mm.disassembly.order.texts/o2m-form"
	_description = "Disassembly Order Texts"

class ViewModelO2MListMmDisassemblyOrderTexts(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.texts"
	_view_name = "mm.disassembly.order.texts/o2m-list"
	_description = "Disassembly Order Texts"
