from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestPaymentSchedules(ViewModelFind):
	_name = "model.find.crm.request.payment.schedules"
	_model = "crm.request.payment.schedules"
	_description = "CRM Request Payment Schedules"
	_columns = ['request_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MFormCrmRequestPaymentSchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.payment.schedules"
	_model = "crm.request.payment.schedules"
	_description = "CRM Request Payment Schedules"
	_columns = ['request_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MListCrmRequestPaymentSchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.payment.schedules"
	_model = "crm.request.payment.schedules"
	_description = "CRM Request Payment Schedules"
	_columns = ['request_id', 'amount', 'currency', 'schedule', 'note']
