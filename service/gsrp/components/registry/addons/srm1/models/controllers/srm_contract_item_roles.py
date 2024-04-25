from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractItemRoles(ViewModelFindController):
	_name = "find:srm.contract.item.roles"
	_view_name = "srm.contract.item.roles/find"
	_description = "SRM Contract Roles"

class ViewModelO2MFormSrmContractItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.item.roles"
	_view_name = "srm.contract.item.roles/o2m-form"
	_description = "SRM Contract Roles"

class ViewModelO2MListSrmContractItemRoles(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.item.roles"
	_view_name = "srm.contract.item.roles/o2m-list"
	_description = "SRM Contract Roles"
