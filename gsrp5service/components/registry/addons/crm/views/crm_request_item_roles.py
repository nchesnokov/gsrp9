from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestItemRoles(ViewModelFind):
	_name = "model.find.crm.request.item.roles"
	_model = "crm.request.item.roles"
	_description = "CRM Request Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmRequestItemRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.item.roles"
	_model = "crm.request.item.roles"
	_description = "CRM Request Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmRequestItemRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.item.roles"
	_model = "crm.request.item.roles"
	_description = "CRM Request Roles"
	_columns = ['item_id', 'role_id', 'patner_id']
