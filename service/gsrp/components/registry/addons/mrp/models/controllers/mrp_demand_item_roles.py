from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandItemRoles(ViewModelFindController):
	_name = "find:mrp.demand.item.roles"
	_view_name = "mrp.demand.item.roles/find"
	_description = "MRP Demand Roles"

class ViewModelO2MFormMrpDemandItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.item.roles"
	_view_name = "mrp.demand.item.roles/o2m-form"
	_description = "MRP Demand Roles"

class ViewModelO2MListMrpDemandItemRoles(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.item.roles"
	_view_name = "mrp.demand.item.roles/o2m-list"
	_description = "MRP Demand Roles"
