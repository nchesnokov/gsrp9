from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmChannels(ViewModelSearch):
	_name = "model.search.crm.channels"
	_model = "crm.channels"
	_description = "CRM Channels"
	_columns = ['category_id', 'code', 'descr']

class ViewModelFindCrmChannels(ViewModelFind):
	_name = "model.find.crm.channels"
	_model = "crm.channels"
	_description = "CRM Channels"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MFormCrmChannels(ViewModelO2MForm):
	_name = "model.o2mform.crm.channels"
	_model = "crm.channels"
	_description = "CRM Channels"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MListCrmChannels(ViewModelO2MList):
	_name = "model.o2mlist.crm.channels"
	_model = "crm.channels"
	_description = "CRM Channels"
	_columns = ['category_id', 'code', 'descr']
