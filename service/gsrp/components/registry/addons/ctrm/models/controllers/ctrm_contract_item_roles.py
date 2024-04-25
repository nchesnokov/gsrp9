from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmContractItemRoles(ViewModelFindController):
	_name = "find:ctrm.contract.item.roles"
	_view_name = "ctrm.contract.item.roles/find"
	_description = "CTRM Contract Item Roles"

class ViewModelO2MFormCtrmContractItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.contract.item.roles"
	_view_name = "ctrm.contract.item.roles/o2m-form"
	_description = "CTRM Contract Item Roles"

class ViewModelO2MListCtrmContractItemRoles(ViewModelO2MListController):
	_name = "o2m-list:ctrm.contract.item.roles"
	_view_name = "ctrm.contract.item.roles/o2m-list"
	_description = "CTRM Contract Item Roles"
