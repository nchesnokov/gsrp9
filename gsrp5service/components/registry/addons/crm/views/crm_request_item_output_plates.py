from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestItemOutputPlates(ViewModelFind):
	_name = "model.find.crm.request.item.output.plates"
	_model = "crm.request.item.output.plates"
	_description = "CRM Request Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MFormCrmRequestItemOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.item.output.plates"
	_model = "crm.request.item.output.plates"
	_description = "CRM Request Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListCrmRequestItemOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.item.output.plates"
	_model = "crm.request.item.output.plates"
	_description = "CRM Request Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']
