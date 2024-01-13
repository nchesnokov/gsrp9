from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractItemOutputPlates(ViewModelFind):
	_name = "model.find.crm.contract.item.output.plates"
	_model = "crm.contract.item.output.plates"
	_description = "Crm Contract Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelO2MFormCrmContractItemOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.item.output.plates"
	_model = "crm.contract.item.output.plates"
	_description = "Crm Contract Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelKanbanCrmContractItemOutputPlates(ViewModelKanban):
	_name = "model.kanban.crm.contract.item.output.plates"
	_model = "crm.contract.item.output.plates"
	_description = "Crm Contract Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MKanbanCrmContractItemOutputPlates(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.contract.item.output.plates"
	_model = "crm.contract.item.output.plates"
	_description = "Crm Contract Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListCrmContractItemOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.item.output.plates"
	_model = "crm.contract.item.output.plates"
	_description = "Crm Contract Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']
