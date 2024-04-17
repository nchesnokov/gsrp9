from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanItemOutputPlates(ViewModelFindController):
	_name = "find:srm.plan.item.output.plates"
	_view_name = "srm.plan.item.output.plates/find"
	_description = "Plan Item Output Plates"

class ViewModelO2MFormSrmPlanItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.item.output.plates"
	_view_name = "srm.plan.item.output.plates/o2m-form"
	_description = "Plan Item Output Plates"

class ViewModelO2MKanbanSrmPlanItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:srm.plan.item.output.plates"
	_view_name = "srm.plan.item.output.plates/o2m-kanban"
	_description = "Plan Item Output Plates"

class ViewModelO2MListSrmPlanItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.item.output.plates"
	_view_name = "srm.plan.item.output.plates/o2m-list"
	_description = "Plan Item Output Plates"
