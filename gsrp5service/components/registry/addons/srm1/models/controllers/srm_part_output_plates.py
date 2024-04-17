from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartOutputPlates(ViewModelFindController):
	_name = "find:srm.part.output.plates"
	_view_name = "srm.part.output.plates/find"
	_description = "SRM Part Output Plates"

class ViewModelO2MFormSrmPartOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.output.plates"
	_view_name = "srm.part.output.plates/o2m-form"
	_description = "SRM Part Output Plates"

class ViewModelO2MKanbanSrmPartOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.part.output.plates"
	_view_name = "srm.part.output.plates/o2m-kanban"
	_description = "SRM Part Output Plates"

class ViewModelO2MListSrmPartOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.part.output.plates"
	_view_name = "srm.part.output.plates/o2m-list"
	_description = "SRM Part Output Plates"
