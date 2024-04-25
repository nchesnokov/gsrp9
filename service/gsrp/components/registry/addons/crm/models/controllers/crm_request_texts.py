from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestTexts(ViewModelFindController):
	_name = "find:crm.request.texts"
	_view_name = "crm.request.texts/find"
	_description = "CRM Request Texts"

class ViewModelO2MFormCrmRequestTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.texts"
	_view_name = "crm.request.texts/o2m-form"
	_description = "CRM Request Texts"

class ViewModelO2MListCrmRequestTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.request.texts"
	_view_name = "crm.request.texts/o2m-list"
	_description = "CRM Request Texts"
