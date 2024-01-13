from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractTypeRoles(ViewModelFind):
	_name = "model.find.crm.contract.type.roles"
	_model = "crm.contract.type.roles"
	_description = "Role Contract Types"
	_columns = ['type_id', 'role_id']

class ViewModelO2MFormCrmContractTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.type.roles"
	_model = "crm.contract.type.roles"
	_description = "Role Contract Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MListCrmContractTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.type.roles"
	_model = "crm.contract.type.roles"
	_description = "Role Contract Types"
	_columns = ['type_id', 'role_id']
