from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestOutputPlates(ViewModelFind):
	_name = "model.find.crm.request.output.plates"
	_model = "crm.request.output.plates"
	_description = "CRM Request Output Plates"
	_columns = ['request_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MFormCrmRequestOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.output.plates"
	_model = "crm.request.output.plates"
	_description = "CRM Request Output Plates"
	_columns = ['request_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListCrmRequestOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.output.plates"
	_model = "crm.request.output.plates"
	_description = "CRM Request Output Plates"
	_columns = ['request_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']
