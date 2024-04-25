from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInternalDeliveryItemTexts(ViewModelFind):
	_name = "model.find.le.internal.delivery.item.texts"
	_model = "le.internal.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelListLeInternalDeliveryItemTexts(ViewModelList):
	_name = "model.list.le.internal.delivery.item.texts"
	_model = "le.internal.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelFormModalLeInternalDeliveryItemTexts(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.item.texts"
	_model = "le.internal.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelFormLeInternalDeliveryItemTexts(ViewModelForm):
	_name = "model.form.le.internal.delivery.item.texts"
	_model = "le.internal.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormLeInternalDeliveryItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.item.texts"
	_model = "le.internal.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListLeInternalDeliveryItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.item.texts"
	_model = "le.internal.delivery.item.texts"
	_description = "Inbound Delivery Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']
