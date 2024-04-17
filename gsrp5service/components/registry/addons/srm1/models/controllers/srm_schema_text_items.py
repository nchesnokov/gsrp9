from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmSchemaTextItems(ViewModelFindController):
	_name = "find:srm.schema.text.items"
	_view_name = "srm.schema.text.items/find"
	_description = "Items Of Schema SRM Texts"

class ViewModelO2MFormSrmSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.schema.text.items"
	_view_name = "srm.schema.text.items/o2m-form"
	_description = "Items Of Schema SRM Texts"

class ViewModelO2MListSrmSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:srm.schema.text.items"
	_view_name = "srm.schema.text.items/o2m-list"
	_description = "Items Of Schema SRM Texts"
