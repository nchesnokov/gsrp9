from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmSubdivisions(ViewModelSearch):
	_name = "model.search.crm.subdivisions"
	_model = "crm.subdivisions"
	_description = "CRM Subdivisions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelFindCrmSubdivisions(ViewModelFind):
	_name = "model.find.crm.subdivisions"
	_model = "crm.subdivisions"
	_description = "CRM Subdivisions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MFormCrmSubdivisions(ViewModelO2MForm):
	_name = "model.o2mform.crm.subdivisions"
	_model = "crm.subdivisions"
	_description = "CRM Subdivisions"
	_columns = ['category_id', 'code', 'descr']

class ViewModelO2MListCrmSubdivisions(ViewModelO2MList):
	_name = "model.o2mlist.crm.subdivisions"
	_model = "crm.subdivisions"
	_description = "CRM Subdivisions"
	_columns = ['category_id', 'code', 'descr']
