from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmContractItems(ViewModelFindController):
	_name = "find:ctrm.contract.items"
	_view_name = "ctrm.contract.items/find"
	_description = "CTRM Offer Items"

class ViewModelO2MFormCtrmContractItems(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.contract.items"
	_view_name = "ctrm.contract.items/o2m-form"
	_description = "CTRM Offer Items"

class ViewModelO2MListCtrmContractItems(ViewModelO2MListController):
	_name = "o2m-list:ctrm.contract.items"
	_view_name = "ctrm.contract.items/o2m-list"
	_description = "CTRM Offer Items"
