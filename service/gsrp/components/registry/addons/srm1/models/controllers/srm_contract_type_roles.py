from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractTypeRoles(ViewModelFindController):
	_name = "find:srm.contract.type.roles"
	_view_name = "srm.contract.type.roles/find"
	_description = "Role SRM Contract Types"

class ViewModelO2MFormSrmContractTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.type.roles"
	_view_name = "srm.contract.type.roles/o2m-form"
	_description = "Role SRM Contract Types"

class ViewModelO2MListSrmContractTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.type.roles"
	_view_name = "srm.contract.type.roles/o2m-list"
	_description = "Role SRM Contract Types"
