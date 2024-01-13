from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchLeDeliverySchemaTexts(ViewModelSearch):
	_name = "model.search.le.delivery.schema.texts"
	_model = "le.delivery.schema.texts"
	_description = "Schema Of Delivery Texts"
	_columns = ['usage', 'code', 'descr']

class ViewModelFindLeDeliverySchemaTexts(ViewModelFind):
	_name = "model.find.le.delivery.schema.texts"
	_model = "le.delivery.schema.texts"
	_description = "Schema Of Delivery Texts"
	_columns = ['usage', 'code', 'descr']

class ViewModelListLeDeliverySchemaTexts(ViewModelList):
	_name = "model.list.le.delivery.schema.texts"
	_model = "le.delivery.schema.texts"
	_description = "Schema Of Delivery Texts"
	_columns = ['usage', 'code', 'descr', 'texts']

class ViewModelFormModalLeDeliverySchemaTexts(ViewModelFormModal):
	_name = "model.form.modal.le.delivery.schema.texts"
	_model = "le.delivery.schema.texts"
	_description = "Schema Of Delivery Texts"
	_columns = ['usage', 'code', 'descr', 'texts']

class ViewModelFormLeDeliverySchemaTexts(ViewModelForm):
	_name = "model.form.le.delivery.schema.texts"
	_model = "le.delivery.schema.texts"
	_description = "Schema Of Delivery Texts"
	_columns = ['usage', 'code', 'descr', 'texts']
