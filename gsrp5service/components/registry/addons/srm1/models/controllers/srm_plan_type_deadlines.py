from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanTypeDeadlines(ViewModelFindController):
	_name = "find:srm.plan.type.deadlines"
	_view_name = "srm.plan.type.deadlines/find"
	_description = "Deadlines SRM Plan Types"

class ViewModelO2MFormSrmPlanTypeDeadlines(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.type.deadlines"
	_view_name = "srm.plan.type.deadlines/o2m-form"
	_description = "Deadlines SRM Plan Types"

class ViewModelO2MListSrmPlanTypeDeadlines(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.type.deadlines"
	_view_name = "srm.plan.type.deadlines/o2m-list"
	_description = "Deadlines SRM Plan Types"
