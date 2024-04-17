from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmSchemaTexts(ViewModelSearchController):
	_name = "search:srm.schema.texts"
	_view_name = "srm.schema.texts/search"
	_description = "Schema Of SRM Texts"

class ViewModelFindSrmSchemaTexts(ViewModelFindController):
	_name = "find:srm.schema.texts"
	_view_name = "srm.schema.texts/find"
	_description = "Schema Of SRM Texts"

class ViewModelListSrmSchemaTexts(ViewModelListController):
	_name = "list:srm.schema.texts"
	_view_name = "srm.schema.texts/list"
	_description = "Schema Of SRM Texts"

class ViewModelFormModalSrmSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:srm.schema.texts"
	_view_name = "srm.schema.texts/form.modal"
	_description = "Schema Of SRM Texts"

class ViewModelFormSrmSchemaTexts(ViewModelFormController):
	_name = "form:srm.schema.texts"
	_view_name = "srm.schema.texts/form"
	_description = "Schema Of SRM Texts"
