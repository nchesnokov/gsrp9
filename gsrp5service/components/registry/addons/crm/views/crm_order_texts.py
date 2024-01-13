from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderTexts(ViewModelFind):
	_name = "model.find.crm.order.texts"
	_model = "crm.order.texts"
	_description = "CRM Order Texts"
	_columns = ['order_id', 'seq', 'text_id', 'descr']

class ViewModelO2MFormCrmOrderTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.texts"
	_model = "crm.order.texts"
	_description = "CRM Order Texts"
	_columns = ['order_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmOrderTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.texts"
	_model = "crm.order.texts"
	_description = "CRM Order Texts"
	_columns = ['order_id', 'seq', 'text_id', 'descr']
