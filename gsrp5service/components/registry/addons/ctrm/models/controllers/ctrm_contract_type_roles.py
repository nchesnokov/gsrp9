from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmContractTypeRoles(ViewModelFindController):
	_name = "find:ctrm.contract.type.roles"
	_view_name = "ctrm.contract.type.roles/find"
	_description = "Role CTRM Contract Types"

class ViewModelO2MFormCtrmContractTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.contract.type.roles"
	_view_name = "ctrm.contract.type.roles/o2m-form"
	_description = "Role CTRM Contract Types"

class ViewModelO2MListCtrmContractTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.contract.type.roles"
	_view_name = "ctrm.contract.type.roles/o2m-list"
	_description = "Role CTRM Contract Types"
