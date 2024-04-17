from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanTexts(ViewModelFindController):
	_name = "find:srm.plan.texts"
	_view_name = "srm.plan.texts/find"
	_description = "SRM Plan Texts"

class ViewModelO2MFormSrmPlanTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.texts"
	_view_name = "srm.plan.texts/o2m-form"
	_description = "SRM Plan Texts"

class ViewModelO2MListSrmPlanTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.texts"
	_view_name = "srm.plan.texts/o2m-list"
	_description = "SRM Plan Texts"
