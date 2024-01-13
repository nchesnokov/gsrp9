from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderOutputPlates(ViewModelFind):
	_name = "model.find.crm.order.output.plates"
	_model = "crm.order.output.plates"
	_description = "CRM Order Output Plates"
	_columns = ['order_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelO2MFormCrmOrderOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.output.plates"
	_model = "crm.order.output.plates"
	_description = "CRM Order Output Plates"
	_columns = ['order_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelKanbanCrmOrderOutputPlates(ViewModelKanban):
	_name = "model.kanban.crm.order.output.plates"
	_model = "crm.order.output.plates"
	_description = "CRM Order Output Plates"
	_columns = ['order_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MKanbanCrmOrderOutputPlates(ViewModelO2MKanban):
	_name = "model.o2mkanban.crm.order.output.plates"
	_model = "crm.order.output.plates"
	_description = "CRM Order Output Plates"
	_columns = ['order_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListCrmOrderOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.output.plates"
	_model = "crm.order.output.plates"
	_description = "CRM Order Output Plates"
	_columns = ['order_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']
