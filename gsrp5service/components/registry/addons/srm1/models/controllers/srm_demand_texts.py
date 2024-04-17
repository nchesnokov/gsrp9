from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandTexts(ViewModelFindController):
	_name = "find:srm.demand.texts"
	_view_name = "srm.demand.texts/find"
	_description = "SRM Demand Texts"

class ViewModelO2MFormSrmDemandTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.texts"
	_view_name = "srm.demand.texts/o2m-form"
	_description = "SRM Demand Texts"

class ViewModelO2MListSrmDemandTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.texts"
	_view_name = "srm.demand.texts/o2m-list"
	_description = "SRM Demand Texts"
