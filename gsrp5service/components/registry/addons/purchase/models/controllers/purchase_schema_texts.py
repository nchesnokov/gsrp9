from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseSchemaTexts(ViewModelSearchController):
	_name = "search:purchase.schema.texts"
	_view_name = "purchase.schema.texts/search"
	_description = "Schema Of Purchase Texts"

class ViewModelFindPurchaseSchemaTexts(ViewModelFindController):
	_name = "find:purchase.schema.texts"
	_view_name = "purchase.schema.texts/find"
	_description = "Schema Of Purchase Texts"

class ViewModelListPurchaseSchemaTexts(ViewModelListController):
	_name = "list:purchase.schema.texts"
	_view_name = "purchase.schema.texts/list"
	_description = "Schema Of Purchase Texts"

class ViewModelFormModalPurchaseSchemaTexts(ViewModelFormModalController):
	_name = "form.modal:purchase.schema.texts"
	_view_name = "purchase.schema.texts/form.modal"
	_description = "Schema Of Purchase Texts"

class ViewModelFormPurchaseSchemaTexts(ViewModelFormController):
	_name = "form:purchase.schema.texts"
	_view_name = "purchase.schema.texts/form"
	_description = "Schema Of Purchase Texts"
