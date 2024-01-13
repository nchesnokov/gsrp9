from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeDeliverySchemaTextItems(ViewModelFind):
	_name = "model.find.le.delivery.schema.text.items"
	_model = "le.delivery.schema.text.items"
	_description = "Items Of Schema Delivery Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']

class ViewModelListLeDeliverySchemaTextItems(ViewModelList):
	_name = "model.list.le.delivery.schema.text.items"
	_model = "le.delivery.schema.text.items"
	_description = "Items Of Schema Delivery Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']

class ViewModelFormModalLeDeliverySchemaTextItems(ViewModelFormModal):
	_name = "model.form.modal.le.delivery.schema.text.items"
	_model = "le.delivery.schema.text.items"
	_description = "Items Of Schema Delivery Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']

class ViewModelFormLeDeliverySchemaTextItems(ViewModelForm):
	_name = "model.form.le.delivery.schema.text.items"
	_model = "le.delivery.schema.text.items"
	_description = "Items Of Schema Delivery Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormLeDeliverySchemaTextItems(ViewModelO2MForm):
	_name = "model.o2mform.le.delivery.schema.text.items"
	_model = "le.delivery.schema.text.items"
	_description = "Items Of Schema Delivery Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']

class ViewModelO2MListLeDeliverySchemaTextItems(ViewModelO2MList):
	_name = "model.o2mlist.le.delivery.schema.text.items"
	_model = "le.delivery.schema.text.items"
	_description = "Items Of Schema Delivery Texts"
	_columns = ['schema_id', 'seq', 'text_id', 'descr']
