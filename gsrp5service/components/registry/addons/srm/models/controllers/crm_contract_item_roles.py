from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractItemRoles(ViewModelFindController):
	_name = "find:crm.contract.item.roles"
	_view_name = "crm.contract.item.roles/find"
	_description = "Crm Contract Roles"

class ViewModelO2MFormCrmContractItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.item.roles"
	_view_name = "crm.contract.item.roles/o2m-form"
	_description = "Crm Contract Roles"

class ViewModelO2MListCrmContractItemRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.item.roles"
	_view_name = "crm.contract.item.roles/o2m-list"
	_description = "Crm Contract Roles"
