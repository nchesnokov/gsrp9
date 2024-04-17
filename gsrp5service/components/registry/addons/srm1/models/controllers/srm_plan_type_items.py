from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanTypeItems(ViewModelFindController):
	_name = "find:srm.plan.type.items"
	_view_name = "srm.plan.type.items/find"
	_description = "Type of SRM Plan Items"

class ViewModelO2MFormSrmPlanTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.type.items"
	_view_name = "srm.plan.type.items/o2m-form"
	_description = "Type of SRM Plan Items"

class ViewModelO2MListSrmPlanTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.type.items"
	_view_name = "srm.plan.type.items/o2m-list"
	_description = "Type of SRM Plan Items"
