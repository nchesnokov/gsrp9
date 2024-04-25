from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmSchemaTexts(ViewModelSearchController):
	_name = "search:mm.schema.texts"
	_view_name = "mm.schema.texts/search"
	_description = "Schema Of Manufactured Texts"

class ViewModelFindMmSchemaTexts(ViewModelFindController):
	_name = "find:mm.schema.texts"
	_view_name = "mm.schema.texts/find"
	_description = "Schema Of Manufactured Texts"

class ViewModelListMmSchemaTexts(ViewModelListController):
	_name = "list:mm.schema.texts"
	_view_name = "mm.schema.texts/list"
	_description = "Schema Of Manufactured Texts"

class ViewModelFormModalMmSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:mm.schema.texts"
	_view_name = "mm.schema.texts/form.modal"
	_description = "Schema Of Manufactured Texts"

class ViewModelFormMmSchemaTexts(ViewModelFormController):
	_name = "form:mm.schema.texts"
	_view_name = "mm.schema.texts/form"
	_description = "Schema Of Manufactured Texts"
