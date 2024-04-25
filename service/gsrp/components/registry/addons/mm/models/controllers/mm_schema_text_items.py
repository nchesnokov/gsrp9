from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmSchemaTextItems(ViewModelFindController):
	_name = "find:mm.schema.text.items"
	_view_name = "mm.schema.text.items/find"
	_description = "Items Of Schema Manufactured Texts"

class ViewModelO2MFormMmSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:mm.schema.text.items"
	_view_name = "mm.schema.text.items/o2m-form"
	_description = "Items Of Schema Manufactured Texts"

class ViewModelO2MListMmSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:mm.schema.text.items"
	_view_name = "mm.schema.text.items/o2m-list"
	_description = "Items Of Schema Manufactured Texts"
