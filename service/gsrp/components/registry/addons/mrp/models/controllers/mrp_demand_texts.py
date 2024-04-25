from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandTexts(ViewModelFindController):
	_name = "find:mrp.demand.texts"
	_view_name = "mrp.demand.texts/find"
	_description = "MRP Demand Texts"

class ViewModelO2MFormMrpDemandTexts(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.texts"
	_view_name = "mrp.demand.texts/o2m-form"
	_description = "MRP Demand Texts"

class ViewModelO2MListMrpDemandTexts(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.texts"
	_view_name = "mrp.demand.texts/o2m-list"
	_description = "MRP Demand Texts"
