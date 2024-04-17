from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandItemTexts(ViewModelFindController):
	_name = "find:srm.demand.item.texts"
	_view_name = "srm.demand.item.texts/find"
	_description = "SRM Demand Item Texts"

class ViewModelO2MFormSrmDemandItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.item.texts"
	_view_name = "srm.demand.item.texts/o2m-form"
	_description = "SRM Demand Item Texts"

class ViewModelO2MListSrmDemandItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.item.texts"
	_view_name = "srm.demand.item.texts/o2m-list"
	_description = "SRM Demand Item Texts"
