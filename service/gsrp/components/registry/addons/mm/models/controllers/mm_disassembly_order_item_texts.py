from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderItemTexts(ViewModelFindController):
	_name = "find:mm.disassembly.order.item.texts"
	_view_name = "mm.disassembly.order.item.texts/find"
	_description = "Disassembly Order Item Texts"

class ViewModelO2MFormMmDisassemblyOrderItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.item.texts"
	_view_name = "mm.disassembly.order.item.texts/o2m-form"
	_description = "Disassembly Order Item Texts"

class ViewModelO2MListMmDisassemblyOrderItemTexts(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.item.texts"
	_view_name = "mm.disassembly.order.item.texts/o2m-list"
	_description = "Disassembly Order Item Texts"
