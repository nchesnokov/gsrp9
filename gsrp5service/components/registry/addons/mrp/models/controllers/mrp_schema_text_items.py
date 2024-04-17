from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMrpSchemaTextItems(ViewModelFindController):
	_name = "find:mrp.schema.text.items"
	_view_name = "mrp.schema.text.items/find"
	_description = "Items Of Schema MRP Texts"

class ViewModelO2MFormMrpSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:mrp.schema.text.items"
	_view_name = "mrp.schema.text.items/o2m-form"
	_description = "Items Of Schema MRP Texts"

class ViewModelO2MListMrpSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:mrp.schema.text.items"
	_view_name = "mrp.schema.text.items/o2m-list"
	_description = "Items Of Schema MRP Texts"
