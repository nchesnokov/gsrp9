from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractItemPaymentSchedules(ViewModelFind):
	_name = "model.find.crm.contract.item.payment.schedules"
	_model = "crm.contract.item.payment.schedules"
	_description = "Crm Contract Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule']

class ViewModelO2MFormCrmContractItemPaymentSchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.item.payment.schedules"
	_model = "crm.contract.item.payment.schedules"
	_description = "Crm Contract Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MListCrmContractItemPaymentSchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.item.payment.schedules"
	_model = "crm.contract.item.payment.schedules"
	_description = "Crm Contract Item Payment Schedules"
	_columns = ['item_id', 'amount', 'currency', 'schedule']
