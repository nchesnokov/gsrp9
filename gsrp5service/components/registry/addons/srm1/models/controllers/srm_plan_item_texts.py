from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmPlanItemTexts(ViewModelFindController):
	_name = "find:srm.plan.item.texts"
	_view_name = "srm.plan.item.texts/find"
	_description = "SRM Plan Item Texts"

class ViewModelO2MFormSrmPlanItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.plan.item.texts"
	_view_name = "srm.plan.item.texts/o2m-form"
	_description = "SRM Plan Item Texts"

class ViewModelO2MListSrmPlanItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.plan.item.texts"
	_view_name = "srm.plan.item.texts/o2m-list"
	_description = "SRM Plan Item Texts"
