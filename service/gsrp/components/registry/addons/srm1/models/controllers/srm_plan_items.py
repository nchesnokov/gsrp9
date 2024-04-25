from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanItems(ViewModelFindController):
	_name = "find:srm.plan.items"
	_view_name = "srm.plan.items/find"
	_description = "SRM Plan Item"

class ViewModelO2MFormSrmPlanItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.items"
	_view_name = "srm.plan.items/o2m-form"
	_description = "SRM Plan Item"

class ViewModelO2MListSrmPlanItems(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.items"
	_view_name = "srm.plan.items/o2m-list"
	_description = "SRM Plan Item"
