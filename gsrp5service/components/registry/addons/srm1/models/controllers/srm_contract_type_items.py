from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractTypeItems(ViewModelFindController):
	_name = "find:srm.contract.type.items"
	_view_name = "srm.contract.type.items/find"
	_description = "Type of SRM Contract Items"

class ViewModelO2MFormSrmContractTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.type.items"
	_view_name = "srm.contract.type.items/o2m-form"
	_description = "Type of SRM Contract Items"

class ViewModelO2MListSrmContractTypeItems(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.type.items"
	_view_name = "srm.contract.type.items/o2m-list"
	_description = "Type of SRM Contract Items"
