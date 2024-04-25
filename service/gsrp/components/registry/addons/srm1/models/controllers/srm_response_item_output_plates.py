from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponseItemOutputPlates(ViewModelFindController):
	_name = "find:srm.response.item.output.plates"
	_view_name = "srm.response.item.output.plates/find"
	_description = "Response Item Output Plates"

class ViewModelO2MFormSrmResponseItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.item.output.plates"
	_view_name = "srm.response.item.output.plates/o2m-form"
	_description = "Response Item Output Plates"

class ViewModelO2MKanbanSrmResponseItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.response.item.output.plates"
	_view_name = "srm.response.item.output.plates/o2m-kanban"
	_description = "Response Item Output Plates"

class ViewModelO2MListSrmResponseItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.response.item.output.plates"
	_view_name = "srm.response.item.output.plates/o2m-list"
	_description = "Response Item Output Plates"
