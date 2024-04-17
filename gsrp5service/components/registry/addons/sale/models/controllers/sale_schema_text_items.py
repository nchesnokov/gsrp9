from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleSchemaTextItems(ViewModelFindController):
	_name = "find:sale.schema.text.items"
	_view_name = "sale.schema.text.items/find"
	_description = "Items Of Schema Sale Texts"

class ViewModelO2MFormSaleSchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:sale.schema.text.items"
	_view_name = "sale.schema.text.items/o2m-form"
	_description = "Items Of Schema Sale Texts"

class ViewModelO2MListSaleSchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:sale.schema.text.items"
	_view_name = "sale.schema.text.items/o2m-list"
	_description = "Items Of Schema Sale Texts"
