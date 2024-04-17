from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeDeliverySchemaTextItems(ViewModelFindController):
	_name = "find:le.delivery.schema.text.items"
	_view_name = "le.delivery.schema.text.items/find"
	_description = "Items Of Schema Delivery Texts"

class ViewModelO2MFormLeDeliverySchemaTextItems(ViewModelO2MFormController):
	_name = "o2m-form:le.delivery.schema.text.items"
	_view_name = "le.delivery.schema.text.items/o2m-form"
	_description = "Items Of Schema Delivery Texts"

class ViewModelO2MListLeDeliverySchemaTextItems(ViewModelO2MListController):
	_name = "o2m-list:le.delivery.schema.text.items"
	_view_name = "le.delivery.schema.text.items/o2m-list"
	_description = "Items Of Schema Delivery Texts"
