from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderPaymentSchedules(ViewModelFind):
	_name = "model.find.crm.order.payment.schedules"
	_model = "crm.order.payment.schedules"
	_description = "CRM Order Payment Schedules"
	_columns = ['order_id', 'amount', 'currency', 'schedule']

class ViewModelO2MFormCrmOrderPaymentSchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.payment.schedules"
	_model = "crm.order.payment.schedules"
	_description = "CRM Order Payment Schedules"
	_columns = ['order_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MListCrmOrderPaymentSchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.payment.schedules"
	_model = "crm.order.payment.schedules"
	_description = "CRM Order Payment Schedules"
	_columns = ['order_id', 'amount', 'currency', 'schedule']
