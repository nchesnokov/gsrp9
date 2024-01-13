from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractItemRoles(ViewModelFind):
	_name = "model.find.crm.contract.item.roles"
	_model = "crm.contract.item.roles"
	_description = "Crm Contract Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MFormCrmContractItemRoles(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.item.roles"
	_model = "crm.contract.item.roles"
	_description = "Crm Contract Roles"
	_columns = ['item_id', 'role_id', 'patner_id']

class ViewModelO2MListCrmContractItemRoles(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.item.roles"
	_model = "crm.contract.item.roles"
	_description = "Crm Contract Roles"
	_columns = ['item_id', 'role_id', 'patner_id']
