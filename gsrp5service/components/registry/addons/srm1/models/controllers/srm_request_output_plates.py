from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestOutputPlates(ViewModelFindController):
	_name = "find:srm.request.output.plates"
	_view_name = "srm.request.output.plates/find"
	_description = "SRM Request Output Plates"

class ViewModelO2MFormSrmRequestOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.output.plates"
	_view_name = "srm.request.output.plates/o2m-form"
	_description = "SRM Request Output Plates"

class ViewModelO2MKanbanSrmRequestOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.request.output.plates"
	_view_name = "srm.request.output.plates/o2m-kanban"
	_description = "SRM Request Output Plates"

class ViewModelO2MListSrmRequestOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.request.output.plates"
	_view_name = "srm.request.output.plates/o2m-list"
	_description = "SRM Request Output Plates"
