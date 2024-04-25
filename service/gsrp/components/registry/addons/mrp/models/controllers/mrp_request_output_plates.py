from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpRequestOutputPlates(ViewModelFindController):
	_name = "find:mrp.request.output.plates"
	_view_name = "mrp.request.output.plates/find"
	_description = "MRP Request Output Plates"

class ViewModelO2MFormMrpRequestOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:mrp.request.output.plates"
	_view_name = "mrp.request.output.plates/o2m-form"
	_description = "MRP Request Output Plates"

class ViewModelO2MKanbanMrpRequestOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:mrp.request.output.plates"
	_view_name = "mrp.request.output.plates/o2m-kanban"
	_description = "MRP Request Output Plates"

class ViewModelO2MListMrpRequestOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:mrp.request.output.plates"
	_view_name = "mrp.request.output.plates/o2m-list"
	_description = "MRP Request Output Plates"
