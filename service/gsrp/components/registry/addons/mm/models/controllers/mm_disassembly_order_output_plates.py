from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmDisassemblyOrderOutputPlates(ViewModelFindController):
	_name = "find:mm.disassembly.order.output.plates"
	_view_name = "mm.disassembly.order.output.plates/find"
	_description = "Disassembly Order Output Plates"

class ViewModelO2MFormMmDisassemblyOrderOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:mm.disassembly.order.output.plates"
	_view_name = "mm.disassembly.order.output.plates/o2m-form"
	_description = "Disassembly Order Output Plates"

class ViewModelO2MKanbanMmDisassemblyOrderOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:mm.disassembly.order.output.plates"
	_view_name = "mm.disassembly.order.output.plates/o2m-kanban"
	_description = "Disassembly Order Output Plates"

class ViewModelO2MListMmDisassemblyOrderOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:mm.disassembly.order.output.plates"
	_view_name = "mm.disassembly.order.output.plates/o2m-list"
	_description = "Disassembly Order Output Plates"
