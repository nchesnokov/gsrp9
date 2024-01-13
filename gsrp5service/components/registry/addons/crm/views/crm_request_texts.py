from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestTexts(ViewModelFind):
	_name = "model.find.crm.request.texts"
	_model = "crm.request.texts"
	_description = "CRM Request Texts"
	_columns = ['request_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MFormCrmRequestTexts(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.texts"
	_model = "crm.request.texts"
	_description = "CRM Request Texts"
	_columns = ['request_id', 'seq', 'text_id', 'descr', 'content']

class ViewModelO2MListCrmRequestTexts(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.texts"
	_model = "crm.request.texts"
	_description = "CRM Request Texts"
	_columns = ['request_id', 'seq', 'text_id', 'descr', 'content']
