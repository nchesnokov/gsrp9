from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseSchemaTextItems(ViewModelFindController):
	_name = "find:purchase.schema.text.items"
	_view_name = "purchase.schema.text.items/find"
	_description = "Items Of Schema Purchase Texts"

class ViewModelO2MFormPurchaseSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:purchase.schema.text.items"
	_view_name = "purchase.schema.text.items/o2m-form"
	_description = "Items Of Schema Purchase Texts"

class ViewModelO2MListPurchaseSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:purchase.schema.text.items"
	_view_name = "purchase.schema.text.items/o2m-list"
	_description = "Items Of Schema Purchase Texts"
