from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryTexts(ViewModelFind):
	_name = "model.find.le.inbound.delivery.texts"
	_model = "le.inbound.delivery.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']

class ViewModelListLeInboundDeliveryTexts(ViewModelList):
	_name = "model.list.le.inbound.delivery.texts"
	_model = "le.inbound.delivery.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']

class ViewModelFormModalLeInboundDeliveryTexts(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.texts"
	_model = "le.inbound.delivery.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelFormLeInboundDeliveryTexts(ViewModelForm):
	_name = "model.form.le.inbound.delivery.texts"
	_model = "le.inbound.delivery.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormLeInboundDeliveryTexts(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.texts"
	_model = "le.inbound.delivery.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListLeInboundDeliveryTexts(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.texts"
	_model = "le.inbound.delivery.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']
