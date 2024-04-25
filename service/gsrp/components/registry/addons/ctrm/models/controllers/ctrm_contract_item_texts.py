from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmContractItemTexts(ViewModelFindController):
	_name = "find:ctrm.contract.item.texts"
	_view_name = "ctrm.contract.item.texts/find"
	_description = "CTRM Contract Item Texts"

class ViewModelO2MFormCtrmContractItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.contract.item.texts"
	_view_name = "ctrm.contract.item.texts/o2m-form"
	_description = "CTRM Contract Item Texts"

class ViewModelO2MListCtrmContractItemTexts(ViewModelO2MListController):
	_name = "o2m-list:ctrm.contract.item.texts"
	_view_name = "ctrm.contract.item.texts/o2m-list"
	_description = "CTRM Contract Item Texts"
