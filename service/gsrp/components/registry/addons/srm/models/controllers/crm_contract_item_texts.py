from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractItemTexts(ViewModelFindController):
	_name = "find:crm.contract.item.texts"
	_view_name = "crm.contract.item.texts/find"
	_description = "Crm Contract Item Texts"

class ViewModelO2MFormCrmContractItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.item.texts"
	_view_name = "crm.contract.item.texts/o2m-form"
	_description = "Crm Contract Item Texts"

class ViewModelO2MListCrmContractItemTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.item.texts"
	_view_name = "crm.contract.item.texts/o2m-list"
	_description = "Crm Contract Item Texts"
