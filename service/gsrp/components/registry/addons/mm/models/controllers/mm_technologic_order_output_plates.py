from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderOutputPlates(ViewModelFindController):
	_name = "find:mm.technologic.order.output.plates"
	_view_name = "mm.technologic.order.output.plates/find"
	_description = "Technologic Order Output Plates"

class ViewModelO2MFormMmTechnologicOrderOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.output.plates"
	_view_name = "mm.technologic.order.output.plates/o2m-form"
	_description = "Technologic Order Output Plates"

class ViewModelO2MKanbanMmTechnologicOrderOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:mm.technologic.order.output.plates"
	_view_name = "mm.technologic.order.output.plates/o2m-kanban"
	_description = "Technologic Order Output Plates"

class ViewModelO2MListMmTechnologicOrderOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.output.plates"
	_view_name = "mm.technologic.order.output.plates/o2m-list"
	_description = "Technologic Order Output Plates"
