from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandItems(ViewModelFindController):
	_name = "find:mrp.demand.items"
	_view_name = "mrp.demand.items/find"
	_description = "MRP Demand Item"

class ViewModelO2MFormMrpDemandItems(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.items"
	_view_name = "mrp.demand.items/o2m-form"
	_description = "MRP Demand Item"

class ViewModelO2MListMrpDemandItems(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.items"
	_view_name = "mrp.demand.items/o2m-list"
	_description = "MRP Demand Item"
