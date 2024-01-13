from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInternalDeliveryTexts(ViewModelFind):
	_name = "model.find.le.internal.delivery.texts"
	_model = "le.internal.delivery.texts"
	_description = "Internal Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']

class ViewModelListLeInternalDeliveryTexts(ViewModelList):
	_name = "model.list.le.internal.delivery.texts"
	_model = "le.internal.delivery.texts"
	_description = "Internal Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']

class ViewModelFormModalLeInternalDeliveryTexts(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.texts"
	_model = "le.internal.delivery.texts"
	_description = "Internal Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelFormLeInternalDeliveryTexts(ViewModelForm):
	_name = "model.form.le.internal.delivery.texts"
	_model = "le.internal.delivery.texts"
	_description = "Internal Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormLeInternalDeliveryTexts(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.texts"
	_model = "le.internal.delivery.texts"
	_description = "Internal Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListLeInternalDeliveryTexts(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.texts"
	_model = "le.internal.delivery.texts"
	_description = "Internal Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']
