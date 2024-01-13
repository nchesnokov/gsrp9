from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderItemOutputPlates(ViewModelFind):
	_name = "model.find.crm.order.item.output.plates"
	_model = "crm.order.item.output.plates"
	_description = "CRM Order Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelO2MFormCrmOrderItemOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.item.output.plates"
	_model = "crm.order.item.output.plates"
	_description = "CRM Order Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelKanbanCrmOrderItemOutputPlates(ViewModelKanban):
	_name = "model.kanban.crm.order.item.output.plates"
	_model = "crm.order.item.output.plates"
	_description = "CRM Order Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MKanbanCrmOrderItemOutputPlates(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.order.item.output.plates"
	_model = "crm.order.item.output.plates"
	_description = "CRM Order Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListCrmOrderItemOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.item.output.plates"
	_model = "crm.order.item.output.plates"
	_description = "CRM Order Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']
