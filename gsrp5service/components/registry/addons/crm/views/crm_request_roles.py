from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestRoles(ViewModelFind):
	_name = "model.find.crm.request.roles"
	_model = "crm.request.roles"
	_description = "CRM Request Roles"
	_columns = ['request_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmRequestRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.roles"
	_model = "crm.request.roles"
	_description = "CRM Request Roles"
	_columns = ['request_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmRequestRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.roles"
	_model = "crm.request.roles"
	_description = "CRM Request Roles"
	_columns = ['request_id', 'role_id', 'patner_id']
