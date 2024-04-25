from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandItemTexts(ViewModelFindController):
	_name = "find:mrp.demand.item.texts"
	_view_name = "mrp.demand.item.texts/find"
	_description = "MRP Demand Item Texts"

class ViewModelO2MFormMrpDemandItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.item.texts"
	_view_name = "mrp.demand.item.texts/o2m-form"
	_description = "MRP Demand Item Texts"

class ViewModelO2MListMrpDemandItemTexts(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.item.texts"
	_view_name = "mrp.demand.item.texts/o2m-list"
	_description = "MRP Demand Item Texts"
