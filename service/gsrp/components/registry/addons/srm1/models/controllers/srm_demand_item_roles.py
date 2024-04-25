from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandItemRoles(ViewModelFindController):
	_name = "find:srm.demand.item.roles"
	_view_name = "srm.demand.item.roles/find"
	_description = "SRM Demand Roles"

class ViewModelO2MFormSrmDemandItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.item.roles"
	_view_name = "srm.demand.item.roles/o2m-form"
	_description = "SRM Demand Roles"

class ViewModelO2MListSrmDemandItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.item.roles"
	_view_name = "srm.demand.item.roles/o2m-list"
	_description = "SRM Demand Roles"
