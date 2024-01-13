from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractOutputPlates(ViewModelFind):
	_name = "model.find.crm.contract.output.plates"
	_model = "crm.contract.output.plates"
	_description = "Crm Contract Output Plates"
	_columns = ['contract_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelO2MFormCrmContractOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.output.plates"
	_model = "crm.contract.output.plates"
	_description = "Crm Contract Output Plates"
	_columns = ['contract_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelKanbanCrmContractOutputPlates(ViewModelKanban):
	_name = "model.kanban.crm.contract.output.plates"
	_model = "crm.contract.output.plates"
	_description = "Crm Contract Output Plates"
	_columns = ['contract_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MKanbanCrmContractOutputPlates(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.contract.output.plates"
	_model = "crm.contract.output.plates"
	_description = "Crm Contract Output Plates"
	_columns = ['contract_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListCrmContractOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.output.plates"
	_model = "crm.contract.output.plates"
	_description = "Crm Contract Output Plates"
	_columns = ['contract_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']
