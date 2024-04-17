from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCtrmSchemaTextItems(ViewModelFindController):
	_name = "find:ctrm.schema.text.items"
	_view_name = "ctrm.schema.text.items/find"
	_description = "Items Of Schema CTRM Texts"

class ViewModelO2MFormCtrmSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:ctrm.schema.text.items"
	_view_name = "ctrm.schema.text.items/o2m-form"
	_description = "Items Of Schema CTRM Texts"

class ViewModelO2MListCtrmSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:ctrm.schema.text.items"
	_view_name = "ctrm.schema.text.items/o2m-list"
	_description = "Items Of Schema CTRM Texts"
