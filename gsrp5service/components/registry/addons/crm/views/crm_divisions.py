from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmDivisions(ViewModelSearch):
	_name = "model.search.crm.divisions"
	_model = "crm.divisions"
	_description = "CRM Divisions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelFindCrmDivisions(ViewModelFind):
	_name = "model.find.crm.divisions"
	_model = "crm.divisions"
	_description = "CRM Divisions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MFormCrmDivisions(ViewModelO2MForm):
	_name = "model.o2mform.crm.divisions"
	_model = "crm.divisions"
	_description = "CRM Divisions"
	_columns = ['category_id', 'code', 'descr', 'subdivisions']

class ViewModelO2MListCrmDivisions(ViewModelO2MList):
	_name = "model.o2mlist.crm.divisions"
	_model = "crm.divisions"
	_description = "CRM Divisions"
	_columns = ['category_id', 'code', 'descr', 'subdivisions']
