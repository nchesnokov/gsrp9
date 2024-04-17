from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjSchemaTexts(ViewModelSearchController):
	_name = "search:prj.schema.texts"
	_view_name = "prj.schema.texts/search"
	_description = "Schema Of Project Texts"

class ViewModelFindPrjSchemaTexts(ViewModelFindController):
	_name = "find:prj.schema.texts"
	_view_name = "prj.schema.texts/find"
	_description = "Schema Of Project Texts"

class ViewModelListPrjSchemaTexts(ViewModelListController):
	_name = "list:prj.schema.texts"
	_view_name = "prj.schema.texts/list"
	_description = "Schema Of Project Texts"

class ViewModelFormModalPrjSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:prj.schema.texts"
	_view_name = "prj.schema.texts/form.modal"
	_description = "Schema Of Project Texts"

class ViewModelFormPrjSchemaTexts(ViewModelFormController):
	_name = "form:prj.schema.texts"
	_view_name = "prj.schema.texts/form"
	_description = "Schema Of Project Texts"
