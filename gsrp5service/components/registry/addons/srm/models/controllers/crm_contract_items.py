from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractItems(ViewModelFindController):
	_name = "find:crm.contract.items"
	_view_name = "crm.contract.items/find"
	_description = "Crm Contract Items"

class ViewModelO2MFormCrmContractItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.items"
	_view_name = "crm.contract.items/o2m-form"
	_description = "Crm Contract Items"

class ViewModelO2MListCrmContractItems(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.items"
	_view_name = "crm.contract.items/o2m-list"
	_description = "Crm Contract Items"
