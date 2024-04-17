from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractTypeRoles(ViewModelFindController):
	_name = "find:crm.contract.type.roles"
	_view_name = "crm.contract.type.roles/find"
	_description = "Role Contract Types"

class ViewModelO2MFormCrmContractTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.type.roles"
	_view_name = "crm.contract.type.roles/o2m-form"
	_description = "Role Contract Types"

class ViewModelO2MListCrmContractTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.type.roles"
	_view_name = "crm.contract.type.roles/o2m-list"
	_description = "Role Contract Types"
