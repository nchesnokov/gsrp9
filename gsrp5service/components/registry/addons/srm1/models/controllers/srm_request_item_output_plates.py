from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestItemOutputPlates(ViewModelFindController):
	_name = "find:srm.request.item.output.plates"
	_view_name = "srm.request.item.output.plates/find"
	_description = "Request Item Output Plates"

class ViewModelO2MFormSrmRequestItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.item.output.plates"
	_view_name = "srm.request.item.output.plates/o2m-form"
	_description = "Request Item Output Plates"

class ViewModelO2MKanbanSrmRequestItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.request.item.output.plates"
	_view_name = "srm.request.item.output.plates/o2m-kanban"
	_description = "Request Item Output Plates"

class ViewModelO2MListSrmRequestItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.request.item.output.plates"
	_view_name = "srm.request.item.output.plates/o2m-list"
	_description = "Request Item Output Plates"
