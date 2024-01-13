from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm

class ViewModelSearchCrmTeams(ViewModelSearch):
	_name = "model.search.crm.teams"
	_model = "crm.teams"
	_description = "CRM Teams"
	_columns = ['division_id', 'subdivision_id', 'fullname', 'note']

class ViewModelFindCrmTeams(ViewModelFind):
	_name = "model.find.crm.teams"
	_model = "crm.teams"
	_description = "CRM Teams"
	_columns = ['division_id', 'subdivision_id', 'fullname', 'note']

class ViewModelListCrmTeams(ViewModelList):
	_name = "model.list.crm.teams"
	_model = "crm.teams"
	_description = "CRM Teams"
	_columns = ['division_id', 'subdivision_id', 'fullname', 'note']

class ViewModelFormModalCrmTeams(ViewModelFormModal):
	_name = "model.form.modal.crm.teams"
	_model = "crm.teams"
	_description = "CRM Teams"
	_columns = ['division_id', 'subdivision_id', 'fullname', 'note']

class ViewModelFormCrmTeams(ViewModelForm):
	_name = "model.form.crm.teams"
	_model = "crm.teams"
	_description = "CRM Teams"
	_columns = ['division_id', 'subdivision_id', 'fullname', 'note']
