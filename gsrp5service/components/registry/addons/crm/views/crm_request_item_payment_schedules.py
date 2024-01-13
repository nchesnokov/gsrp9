from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmRequestItemPaymentSchedules(ViewModelFind):
	_name = "model.find.crm.request.item.payment.schedules"
	_model = "crm.request.item.payment.schedules"
	_description = "CRM Request Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MFormCrmRequestItemPaymentSchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.request.item.payment.schedules"
	_model = "crm.request.item.payment.schedules"
	_description = "CRM Request Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MListCrmRequestItemPaymentSchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.request.item.payment.schedules"
	_model = "crm.request.item.payment.schedules"
	_description = "CRM Request Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule', 'note']
