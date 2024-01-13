from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractTypeItems(ViewModelFind):
	_name = "model.find.crm.contract.type.items"
	_model = "crm.contract.type.items"
	_description = "Role Contract Items"
	_columns = ['type_id', 'gti_id', 'itype_id']

class ViewModelO2MFormCrmContractTypeItems(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.type.items"
	_model = "crm.contract.type.items"
	_description = "Role Contract Items"
	_columns = ['type_id', 'gti_id', 'itype_id', 'note']

class ViewModelO2MListCrmContractTypeItems(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.type.items"
	_model = "crm.contract.type.items"
	_description = "Role Contract Items"
	_columns = ['type_id', 'gti_id', 'itype_id']
