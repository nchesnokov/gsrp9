from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractRoles(ViewModelFind):
	_name = "model.find.crm.contract.roles"
	_model = "crm.contract.roles"
	_description = "Crm Contract Roles"
	_columns = ['contract_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmContractRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.roles"
	_model = "crm.contract.roles"
	_description = "Crm Contract Roles"
	_columns = ['contract_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmContractRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.roles"
	_model = "crm.contract.roles"
	_description = "Crm Contract Roles"
	_columns = ['contract_id', 'role_id', 'patner_id']
