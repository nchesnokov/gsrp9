from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseOutputPlates(ViewModelFindController):
	_name = "find:srm.response.output.plates"
	_view_name = "srm.response.output.plates/find"
	_description = "SRM Response Output Plates"

class ViewModelO2MFormSrmResponseOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.output.plates"
	_view_name = "srm.response.output.plates/o2m-form"
	_description = "SRM Response Output Plates"

class ViewModelO2MKanbanSrmResponseOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.response.output.plates"
	_view_name = "srm.response.output.plates/o2m-kanban"
	_description = "SRM Response Output Plates"

class ViewModelO2MListSrmResponseOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.response.output.plates"
	_view_name = "srm.response.output.plates/o2m-list"
	_description = "SRM Response Output Plates"
