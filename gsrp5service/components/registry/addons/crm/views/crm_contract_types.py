from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchCrmContractTypes(ViewModelSearch):
	_name = "model.search.crm.contract.types"
	_model = "crm.contract.types"
	_description = "Types Contract"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'required']

class ViewModelFindCrmContractTypes(ViewModelFind):
	_name = "model.find.crm.contract.types"
	_model = "crm.contract.types"
	_description = "Types Contract"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'required']

class ViewModelO2MFormCrmContractTypes(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.types"
	_model = "crm.contract.types"
	_description = "Types Contract"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'roles', 'tis', 'required', 'note']

class ViewModelO2MListCrmContractTypes(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.types"
	_model = "crm.contract.types"
	_description = "Types Contract"
	_columns = ['otype', 'name', 'htschema', 'itschema', 'roles', 'tis', 'required']
