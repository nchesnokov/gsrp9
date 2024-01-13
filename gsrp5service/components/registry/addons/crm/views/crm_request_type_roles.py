from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestTypeRoles(ViewModelFind):
	_name = "model.find.crm.request.type.roles"
	_model = "crm.request.type.roles"
	_description = "Role CRM Request Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MFormCrmRequestTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.type.roles"
	_model = "crm.request.type.roles"
	_description = "Role CRM Request Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MListCrmRequestTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.type.roles"
	_model = "crm.request.type.roles"
	_description = "Role CRM Request Types"
	_columns = ['type_id', 'role_id', 'note']
