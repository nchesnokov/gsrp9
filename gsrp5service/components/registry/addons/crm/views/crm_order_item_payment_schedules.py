from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmOrderItemPaymentSchedules(ViewModelFind):
	_name = "model.find.crm.order.item.payment.schedules"
	_model = "crm.order.item.payment.schedules"
	_description = "CRM Order Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule']

class ViewModelO2MFormCrmOrderItemPaymentSchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.order.item.payment.schedules"
	_model = "crm.order.item.payment.schedules"
	_description = "CRM Order Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MListCrmOrderItemPaymentSchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.order.item.payment.schedules"
	_model = "crm.order.item.payment.schedules"
	_description = "CRM Order Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule']
