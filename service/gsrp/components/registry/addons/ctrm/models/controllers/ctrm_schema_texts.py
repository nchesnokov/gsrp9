from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmSchemaTexts(ViewModelSearchController):
	_name = "search:ctrm.schema.texts"
	_view_name = "ctrm.schema.texts/search"
	_description = "Schema Of CTRM Texts"

class ViewModelFindCtrmSchemaTexts(ViewModelFindController):
	_name = "find:ctrm.schema.texts"
	_view_name = "ctrm.schema.texts/find"
	_description = "Schema Of CTRM Texts"

class ViewModelListCtrmSchemaTexts(ViewModelListController):
	_name = "list:ctrm.schema.texts"
	_view_name = "ctrm.schema.texts/list"
	_description = "Schema Of CTRM Texts"

class ViewModelFormModalCtrmSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:ctrm.schema.texts"
	_view_name = "ctrm.schema.texts/form.modal"
	_description = "Schema Of CTRM Texts"

class ViewModelFormCtrmSchemaTexts(ViewModelFormController):
	_name = "form:ctrm.schema.texts"
	_view_name = "ctrm.schema.texts/form"
	_description = "Schema Of CTRM Texts"
