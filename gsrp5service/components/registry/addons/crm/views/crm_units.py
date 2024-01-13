from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelM2MList
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmUnits(ViewModelSearch):
	_name = "model.search.crm.units"
	_model = "crm.units"
	_description = "CRM Units"
	_columns = ['category_id', 'code', 'descr']

class ViewModelFindCrmUnits(ViewModelFind):
	_name = "model.find.crm.units"
	_model = "crm.units"
	_description = "CRM Units"
	_columns = ['category_id', 'code', 'descr']

class ViewModelM2MListCrmUnits(ViewModelM2MList):
	_name = "model.m2mlist.crm.units"
	_model = "crm.units"
	_description = "CRM Units"
	_columns = ['name', 'country', 'currency', 'note']

class ViewModelO2MFormCrmUnits(ViewModelO2MForm):
	_name = "model.o2mform.crm.units"
	_model = "crm.units"
	_description = "CRM Units"
	_columns = ['category_id', 'company_ids', 'code', 'descr', 'channels', 'segments', 'areas', 'regions']

class ViewModelO2MListCrmUnits(ViewModelO2MList):
	_name = "model.o2mlist.crm.units"
	_model = "crm.units"
	_description = "CRM Units"
	_columns = ['category_id', 'code', 'descr', 'channels', 'segments', 'areas', 'regions']
