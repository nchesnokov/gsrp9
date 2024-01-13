from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryItemTexts(ViewModelFind):
	_name = "model.find.le.inbound.delivery.item.texts"
	_model = "le.inbound.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelListLeInboundDeliveryItemTexts(ViewModelList):
	_name = "model.list.le.inbound.delivery.item.texts"
	_model = "le.inbound.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelFormModalLeInboundDeliveryItemTexts(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.item.texts"
	_model = "le.inbound.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelFormLeInboundDeliveryItemTexts(ViewModelForm):
	_name = "model.form.le.inbound.delivery.item.texts"
	_model = "le.inbound.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormLeInboundDeliveryItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.item.texts"
	_model = "le.inbound.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListLeInboundDeliveryItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.item.texts"
	_model = "le.inbound.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']
