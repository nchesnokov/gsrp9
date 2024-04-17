from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmSchemaTextItems(ViewModelFindController):
	_name = "find:crm.schema.text.items"
	_view_name = "crm.schema.text.items/find"
	_description = "Items Of Schema CRM Texts"

class ViewModelO2MFormCrmSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.schema.text.items"
	_view_name = "crm.schema.text.items/o2m-form"
	_description = "Items Of Schema CRM Texts"

class ViewModelO2MListCrmSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:crm.schema.text.items"
	_view_name = "crm.schema.text.items/o2m-list"
	_description = "Items Of Schema CRM Texts"
