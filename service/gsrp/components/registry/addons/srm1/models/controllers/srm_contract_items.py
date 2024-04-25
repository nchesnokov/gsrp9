from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractItems(ViewModelFindController):
	_name = "find:srm.contract.items"
	_view_name = "srm.contract.items/find"
	_description = "SRM Contract Item"

class ViewModelO2MFormSrmContractItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.items"
	_view_name = "srm.contract.items/o2m-form"
	_description = "SRM Contract Item"

class ViewModelO2MListSrmContractItems(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.items"
	_view_name = "srm.contract.items/o2m-list"
	_description = "SRM Contract Item"
