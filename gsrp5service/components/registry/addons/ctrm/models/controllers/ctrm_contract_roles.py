from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmContractRoles(ViewModelFindController):
	_name = "find:ctrm.contract.roles"
	_view_name = "ctrm.contract.roles/find"
	_description = "CTRM Contracts Roles"

class ViewModelO2MFormCtrmContractRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.contract.roles"
	_view_name = "ctrm.contract.roles/o2m-form"
	_description = "CTRM Contracts Roles"

class ViewModelO2MListCtrmContractRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.contract.roles"
	_view_name = "ctrm.contract.roles/o2m-list"
	_description = "CTRM Contracts Roles"
