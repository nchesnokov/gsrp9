from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestItemTexts(ViewModelFindController):
	_name = "find:crm.request.item.texts"
	_view_name = "crm.request.item.texts/find"
	_description = "CRM Request Item Texts"

class ViewModelO2MFormCrmRequestItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.item.texts"
	_view_name = "crm.request.item.texts/o2m-form"
	_description = "CRM Request Item Texts"

class ViewModelO2MListCrmRequestItemTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.request.item.texts"
	_view_name = "crm.request.item.texts/o2m-list"
	_description = "CRM Request Item Texts"
