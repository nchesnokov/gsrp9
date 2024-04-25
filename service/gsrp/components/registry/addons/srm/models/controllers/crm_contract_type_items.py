from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractTypeItems(ViewModelFindController):
	_name = "find:crm.contract.type.items"
	_view_name = "crm.contract.type.items/find"
	_description = "Role Contract Items"

class ViewModelO2MFormCrmContractTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.type.items"
	_view_name = "crm.contract.type.items/o2m-form"
	_description = "Role Contract Items"

class ViewModelO2MListCrmContractTypeItems(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.type.items"
	_view_name = "crm.contract.type.items/o2m-list"
	_description = "Role Contract Items"
