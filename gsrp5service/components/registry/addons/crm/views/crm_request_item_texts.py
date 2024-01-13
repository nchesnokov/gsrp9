from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestItemTexts(ViewModelFind):
	_name = "model.find.crm.request.item.texts"
	_model = "crm.request.item.texts"
	_description = "CRM Request Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormCrmRequestItemTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.item.texts"
	_model = "crm.request.item.texts"
	_description = "CRM Request Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmRequestItemTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.item.texts"
	_model = "crm.request.item.texts"
	_description = "CRM Request Item Texts"
	_columns = ['item_id', 'seq', 'text_id', 'descr', 'content']
