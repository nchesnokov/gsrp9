from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmSchemaTexts(ViewModelSearchController):
	_name = "search:crm.schema.texts"
	_view_name = "crm.schema.texts/search"
	_description = "Schema Of CRM Texts"

class ViewModelFindCrmSchemaTexts(ViewModelFindController):
	_name = "find:crm.schema.texts"
	_view_name = "crm.schema.texts/find"
	_description = "Schema Of CRM Texts"

class ViewModelListCrmSchemaTexts(ViewModelListController):
	_name = "list:crm.schema.texts"
	_view_name = "crm.schema.texts/list"
	_description = "Schema Of CRM Texts"

class ViewModelFormModalCrmSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:crm.schema.texts"
	_view_name = "crm.schema.texts/form.modal"
	_description = "Schema Of CRM Texts"

class ViewModelFormCrmSchemaTexts(ViewModelFormController):
	_name = "form:crm.schema.texts"
	_view_name = "crm.schema.texts/form"
	_description = "Schema Of CRM Texts"
