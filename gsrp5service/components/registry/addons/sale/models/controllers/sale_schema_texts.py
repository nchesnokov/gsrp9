from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleSchemaTexts(ViewModelSearchController):
	_name = "search:sale.schema.texts"
	_view_name = "sale.schema.texts/search"
	_description = "Schema Of Sale Texts"

class ViewModelFindSaleSchemaTexts(ViewModelFindController):
	_name = "find:sale.schema.texts"
	_view_name = "sale.schema.texts/find"
	_description = "Schema Of Sale Texts"

class ViewModelListSaleSchemaTexts(ViewModelListController):
	_name = "list:sale.schema.texts"
	_view_name = "sale.schema.texts/list"
	_description = "Schema Of Sale Texts"

class ViewModelFormModalSaleSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:sale.schema.texts"
	_view_name = "sale.schema.texts/form.modal"
	_description = "Schema Of Sale Texts"

class ViewModelFormSaleSchemaTexts(ViewModelFormController):
	_name = "form:sale.schema.texts"
	_view_name = "sale.schema.texts/form"
	_description = "Schema Of Sale Texts"
