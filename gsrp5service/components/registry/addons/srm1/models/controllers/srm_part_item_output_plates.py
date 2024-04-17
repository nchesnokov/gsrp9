from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPartItemOutputPlates(ViewModelFindController):
	_name = "find:srm.part.item.output.plates"
	_view_name = "srm.part.item.output.plates/find"
	_description = "Part Item Output Plates"

class ViewModelO2MFormSrmPartItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.part.item.output.plates"
	_view_name = "srm.part.item.output.plates/o2m-form"
	_description = "Part Item Output Plates"

class ViewModelO2MKanbanSrmPartItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.part.item.output.plates"
	_view_name = "srm.part.item.output.plates/o2m-kanban"
	_description = "Part Item Output Plates"

class ViewModelO2MListSrmPartItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.part.item.output.plates"
	_view_name = "srm.part.item.output.plates/o2m-list"
	_description = "Part Item Output Plates"
