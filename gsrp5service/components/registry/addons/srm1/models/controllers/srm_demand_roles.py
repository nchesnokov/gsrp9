from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandRoles(ViewModelFindController):
	_name = "find:srm.demand.roles"
	_view_name = "srm.demand.roles/find"
	_description = "SRM Demand Roles"

class ViewModelO2MFormSrmDemandRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.roles"
	_view_name = "srm.demand.roles/o2m-form"
	_description = "SRM Demand Roles"

class ViewModelO2MListSrmDemandRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.roles"
	_view_name = "srm.demand.roles/o2m-list"
	_description = "SRM Demand Roles"
