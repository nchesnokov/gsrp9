from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractRoles(ViewModelFindController):
	_name = "find:crm.contract.roles"
	_view_name = "crm.contract.roles/find"
	_description = "Crm Contract Roles"

class ViewModelO2MFormCrmContractRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.roles"
	_view_name = "crm.contract.roles/o2m-form"
	_description = "Crm Contract Roles"

class ViewModelO2MListCrmContractRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.roles"
	_view_name = "crm.contract.roles/o2m-list"
	_description = "Crm Contract Roles"
