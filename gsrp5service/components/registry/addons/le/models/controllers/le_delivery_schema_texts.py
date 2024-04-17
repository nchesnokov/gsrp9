from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLeDeliverySchemaTexts(ViewModelSearchController):
	_name = "search:le.delivery.schema.texts"
	_view_name = "le.delivery.schema.texts/search"
	_description = "Schema Of Delivery Texts"

class ViewModelFindLeDeliverySchemaTexts(ViewModelFindController):
	_name = "find:le.delivery.schema.texts"
	_view_name = "le.delivery.schema.texts/find"
	_description = "Schema Of Delivery Texts"

class ViewModelListLeDeliverySchemaTexts(ViewModelListController):
	_name = "list:le.delivery.schema.texts"
	_view_name = "le.delivery.schema.texts/list"
	_description = "Schema Of Delivery Texts"

class ViewModelFormModalLeDeliverySchemaTexts(ViewModelFormModalController):
	_name = "form.modal:le.delivery.schema.texts"
	_view_name = "le.delivery.schema.texts/form.modal"
	_description = "Schema Of Delivery Texts"

class ViewModelFormLeDeliverySchemaTexts(ViewModelFormController):
	_name = "form:le.delivery.schema.texts"
	_view_name = "le.delivery.schema.texts/form"
	_description = "Schema Of Delivery Texts"
