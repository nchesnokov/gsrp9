from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmAreas(ViewModelSearch):
	_name = "model.search.crm.areas"
	_model = "crm.areas"
	_description = "CRM Areas"
	_columns = ['category_id', 'code', 'descr']

class ViewModelFindCrmAreas(ViewModelFind):
	_name = "model.find.crm.areas"
	_model = "crm.areas"
	_description = "CRM Areas"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MFormCrmAreas(ViewModelO2MForm):
	_name = "model.o2mform.crm.areas"
	_model = "crm.areas"
	_description = "CRM Areas"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MListCrmAreas(ViewModelO2MList):
	_name = "model.o2mlist.crm.areas"
	_model = "crm.areas"
	_description = "CRM Areas"
	_columns = ['category_id', 'code', 'descr']
