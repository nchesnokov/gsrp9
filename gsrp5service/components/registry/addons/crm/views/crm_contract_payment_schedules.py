from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindCrmContractPaymentSchedules(ViewModelFind):
	_name = "model.find.crm.contract.payment.schedules"
	_model = "crm.contract.payment.schedules"
	_description = "Crm Contract Payment Schedules"
	_columns = ['contract_id', 'amount', 'currency', 'schedule']

class ViewModelO2MFormCrmContractPaymentSchedules(ViewModelO2MForm):
	_name = "model.o2mform.crm.contract.payment.schedules"
	_model = "crm.contract.payment.schedules"
	_description = "Crm Contract Payment Schedules"
	_columns = ['contract_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MListCrmContractPaymentSchedules(ViewModelO2MList):
	_name = "model.o2mlist.crm.contract.payment.schedules"
	_model = "crm.contract.payment.schedules"
	_description = "Crm Contract Payment Schedules"
	_columns = ['contract_id', 'amount', 'currency', 'schedule']
