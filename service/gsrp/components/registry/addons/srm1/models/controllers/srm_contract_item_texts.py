from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractItemTexts(ViewModelFindController):
	_name = "find:srm.contract.item.texts"
	_view_name = "srm.contract.item.texts/find"
	_description = "SRM Contract Item Texts"

class ViewModelO2MFormSrmContractItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.item.texts"
	_view_name = "srm.contract.item.texts/o2m-form"
	_description = "SRM Contract Item Texts"

class ViewModelO2MListSrmContractItemTexts(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.item.texts"
	_view_name = "srm.contract.item.texts/o2m-list"
	_description = "SRM Contract Item Texts"
