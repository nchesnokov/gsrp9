from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeOutboundDeliveryItemTexts(ViewModelFind):
	_name = "model.find.le.outbound.delivery.item.texts"
	_model = "le.outbound.delivery.item.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelListLeOutboundDeliveryItemTexts(ViewModelList):
	_name = "model.list.le.outbound.delivery.item.texts"
	_model = "le.outbound.delivery.item.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelFormModalLeOutboundDeliveryItemTexts(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.item.texts"
	_model = "le.outbound.delivery.item.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelFormLeOutboundDeliveryItemTexts(ViewModelForm):
	_name = "model.form.le.outbound.delivery.item.texts"
	_model = "le.outbound.delivery.item.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormLeOutboundDeliveryItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.item.texts"
	_model = "le.outbound.delivery.item.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListLeOutboundDeliveryItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.item.texts"
	_model = "le.outbound.delivery.item.texts"
	_description = "Outbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']
