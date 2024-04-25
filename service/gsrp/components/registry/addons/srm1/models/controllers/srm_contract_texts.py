from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractTexts(ViewModelFindController):
	_name = "find:srm.contract.texts"
	_view_name = "srm.contract.texts/find"
	_description = "SRM Contract Texts"

class ViewModelO2MFormSrmContractTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.texts"
	_view_name = "srm.contract.texts/o2m-form"
	_description = "SRM Contract Texts"

class ViewModelO2MListSrmContractTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.texts"
	_view_name = "srm.contract.texts/o2m-list"
	_description = "SRM Contract Texts"
