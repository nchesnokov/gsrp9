from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPrjSchemaTextItems(ViewModelFindController):
	_name = "find:prj.schema.text.items"
	_view_name = "prj.schema.text.items/find"
	_description = "Items Of Schema Project Texts"

class ViewModelO2MFormPrjSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:prj.schema.text.items"
	_view_name = "prj.schema.text.items/o2m-form"
	_description = "Items Of Schema Project Texts"

class ViewModelO2MListPrjSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:prj.schema.text.items"
	_view_name = "prj.schema.text.items/o2m-list"
	_description = "Items Of Schema Project Texts"
