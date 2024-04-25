from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanOutputPlates(ViewModelFindController):
	_name = "find:srm.plan.output.plates"
	_view_name = "srm.plan.output.plates/find"
	_description = "SRM Plan Output Plates"

class ViewModelO2MFormSrmPlanOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.output.plates"
	_view_name = "srm.plan.output.plates/o2m-form"
	_description = "SRM Plan Output Plates"

class ViewModelO2MKanbanSrmPlanOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.plan.output.plates"
	_view_name = "srm.plan.output.plates/o2m-kanban"
	_description = "SRM Plan Output Plates"

class ViewModelO2MListSrmPlanOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.output.plates"
	_view_name = "srm.plan.output.plates/o2m-list"
	_description = "SRM Plan Output Plates"
