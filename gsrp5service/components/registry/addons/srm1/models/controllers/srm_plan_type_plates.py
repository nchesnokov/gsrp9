from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanTypePlates(ViewModelFindController):
	_name = "find:srm.plan.type.plates"
	_view_name = "srm.plan.type.plates/find"
	_description = "SRM Plan Plates"

class ViewModelO2MFormSrmPlanTypePlates(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.type.plates"
	_view_name = "srm.plan.type.plates/o2m-form"
	_description = "SRM Plan Plates"

class ViewModelO2MListSrmPlanTypePlates(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.type.plates"
	_view_name = "srm.plan.type.plates/o2m-list"
	_description = "SRM Plan Plates"
