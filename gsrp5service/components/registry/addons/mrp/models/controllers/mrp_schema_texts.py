from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMrpSchemaTexts(ViewModelSearchController):
	_name = "search:mrp.schema.texts"
	_view_name = "mrp.schema.texts/search"
	_description = "Schema Of MRP Texts"

class ViewModelFindMrpSchemaTexts(ViewModelFindController):
	_name = "find:mrp.schema.texts"
	_view_name = "mrp.schema.texts/find"
	_description = "Schema Of MRP Texts"

class ViewModelListMrpSchemaTexts(ViewModelListController):
	_name = "list:mrp.schema.texts"
	_view_name = "mrp.schema.texts/list"
	_description = "Schema Of MRP Texts"

class ViewModelFormModalMrpSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:mrp.schema.texts"
	_view_name = "mrp.schema.texts/form.modal"
	_description = "Schema Of MRP Texts"

class ViewModelFormMrpSchemaTexts(ViewModelFormController):
	_name = "form:mrp.schema.texts"
	_view_name = "mrp.schema.texts/form"
	_description = "Schema Of MRP Texts"
