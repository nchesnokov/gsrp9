from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractRoles(ViewModelFindController):
	_name = "find:srm.contract.roles"
	_view_name = "srm.contract.roles/find"
	_description = "SRM Contract Roles"

class ViewModelO2MFormSrmContractRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.roles"
	_view_name = "srm.contract.roles/o2m-form"
	_description = "SRM Contract Roles"

class ViewModelO2MListSrmContractRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.roles"
	_view_name = "srm.contract.roles/o2m-list"
	_description = "SRM Contract Roles"
