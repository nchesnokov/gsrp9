from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandRoles(ViewModelFindController):
	_name = "find:mrp.demand.roles"
	_view_name = "mrp.demand.roles/find"
	_description = "MRP Demand Roles"

class ViewModelO2MFormMrpDemandRoles(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.roles"
	_view_name = "mrp.demand.roles/o2m-form"
	_description = "MRP Demand Roles"

class ViewModelO2MListMrpDemandRoles(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.roles"
	_view_name = "mrp.demand.roles/o2m-list"
	_description = "MRP Demand Roles"
