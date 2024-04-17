from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmDemandTypeRoles(ViewModelFindController):
	_name = "find:srm.demand.type.roles"
	_view_name = "srm.demand.type.roles/find"
	_description = "Role SRM Demand Types"

class ViewModelO2MFormSrmDemandTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.demand.type.roles"
	_view_name = "srm.demand.type.roles/o2m-form"
	_description = "Role SRM Demand Types"

class ViewModelO2MListSrmDemandTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.demand.type.roles"
	_view_name = "srm.demand.type.roles/o2m-list"
	_description = "Role SRM Demand Types"
