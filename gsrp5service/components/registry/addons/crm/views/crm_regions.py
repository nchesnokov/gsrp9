from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmRegions(ViewModelSearch):
	_name = "model.search.crm.regions"
	_model = "crm.regions"
	_description = "CRM Regions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelFindCrmRegions(ViewModelFind):
	_name = "model.find.crm.regions"
	_model = "crm.regions"
	_description = "CRM Regions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MFormCrmRegions(ViewModelO2MForm):
	_name = "model.o2mform.crm.regions"
	_model = "crm.regions"
	_description = "CRM Regions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MListCrmRegions(ViewModelO2MList):
	_name = "model.o2mlist.crm.regions"
	_model = "crm.regions"
	_description = "CRM Regions"
	_columns = ['category_id', 'code', 'descr']
