from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmContractTexts(ViewModelFindController):
	_name = "find:ctrm.contract.texts"
	_view_name = "ctrm.contract.texts/find"
	_description = "CTRM Contract Texts"

class ViewModelO2MFormCtrmContractTexts(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.contract.texts"
	_view_name = "ctrm.contract.texts/o2m-form"
	_description = "CTRM Contract Texts"

class ViewModelO2MListCtrmContractTexts(ViewModelO2MListController):
	_name = "o2m-list:ctrm.contract.texts"
	_view_name = "ctrm.contract.texts/o2m-list"
	_description = "CTRM Contract Texts"
