from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmSegments(ViewModelSearch):
	_name = "model.search.crm.segments"
	_model = "crm.segments"
	_description = "CRM Segments"
	_columns = ['category_id', 'code', 'descr']

class ViewModelFindCrmSegments(ViewModelFind):
	_name = "model.find.crm.segments"
	_model = "crm.segments"
	_description = "CRM Segments"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MFormCrmSegments(ViewModelO2MForm):
	_name = "model.o2mform.crm.segments"
	_model = "crm.segments"
	_description = "CRM Segments"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MListCrmSegments(ViewModelO2MList):
	_name = "model.o2mlist.crm.segments"
	_model = "crm.segments"
	_description = "CRM Segments"
	_columns = ['category_id', 'code', 'descr']
