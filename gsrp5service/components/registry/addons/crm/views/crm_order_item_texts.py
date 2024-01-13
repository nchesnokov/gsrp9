from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderItemTexts(ViewModelFind):
	_name = "model.find.crm.order.item.texts"
	_model = "crm.order.item.texts"
	_description = "CRM Order Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormCrmOrderItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.item.texts"
	_model = "crm.order.item.texts"
	_description = "CRM Order Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmOrderItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.item.texts"
	_model = "crm.order.item.texts"
	_description = "CRM Order Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr']
