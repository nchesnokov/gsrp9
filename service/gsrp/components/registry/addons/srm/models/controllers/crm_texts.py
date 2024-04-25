from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmTexts(ViewModelSearchController):
	_name = "search:crm.texts"
	_view_name = "crm.texts/search"
	_description = "CRM Texts"

class ViewModelFindCrmTexts(ViewModelFindController):
	_name = "find:crm.texts"
	_view_name = "crm.texts/find"
	_description = "CRM Texts"

class ViewModelListCrmTexts(ViewModelListController):
	_name = "list:crm.texts"
	_view_name = "crm.texts/list"
	_description = "CRM Texts"

class ViewModelFormModalCrmTexts(ViewModelFormModalController):
	_name = "form.modal:crm.texts"
	_view_name = "crm.texts/form.modal"
	_description = "CRM Texts"

class ViewModelFormCrmTexts(ViewModelFormController):
	_name = "form:crm.texts"
	_view_name = "crm.texts/form"
	_description = "CRM Texts"
