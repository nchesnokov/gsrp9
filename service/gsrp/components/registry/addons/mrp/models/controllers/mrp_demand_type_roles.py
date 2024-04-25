from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpDemandTypeRoles(ViewModelFindController):
	_name = "find:mrp.demand.type.roles"
	_view_name = "mrp.demand.type.roles/find"
	_description = "Role MRP Demand Types"

class ViewModelO2MFormMrpDemandTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:mrp.demand.type.roles"
	_view_name = "mrp.demand.type.roles/o2m-form"
	_description = "Role MRP Demand Types"

class ViewModelO2MListMrpDemandTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:mrp.demand.type.roles"
	_view_name = "mrp.demand.type.roles/o2m-list"
	_description = "Role MRP Demand Types"
