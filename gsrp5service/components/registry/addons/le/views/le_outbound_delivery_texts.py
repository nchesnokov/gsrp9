from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeOutboundDeliveryTexts(ViewModelFind):
	_name = "model.find.le.outbound.delivery.texts"
	_model = "le.outbound.delivery.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']

class ViewModelListLeOutboundDeliveryTexts(ViewModelList):
	_name = "model.list.le.outbound.delivery.texts"
	_model = "le.outbound.delivery.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']

class ViewModelFormModalLeOutboundDeliveryTexts(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.texts"
	_model = "le.outbound.delivery.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelFormLeOutboundDeliveryTexts(ViewModelForm):
	_name = "model.form.le.outbound.delivery.texts"
	_model = "le.outbound.delivery.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormLeOutboundDeliveryTexts(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.texts"
	_model = "le.outbound.delivery.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListLeOutboundDeliveryTexts(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.texts"
	_model = "le.outbound.delivery.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['delivery_id', 'seq', 'text_id', 'descr']
