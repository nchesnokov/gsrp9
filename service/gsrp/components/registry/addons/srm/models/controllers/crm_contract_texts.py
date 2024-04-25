from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractTexts(ViewModelFindController):
	_name = "find:crm.contract.texts"
	_view_name = "crm.contract.texts/find"
	_description = "Crm Contract Texts"

class ViewModelO2MFormCrmContractTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.texts"
	_view_name = "crm.contract.texts/o2m-form"
	_description = "Crm Contract Texts"

class ViewModelO2MListCrmContractTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.texts"
	_view_name = "crm.contract.texts/o2m-list"
	_description = "Crm Contract Texts"
