from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractPaymentSchedules(ViewModelFindController):
	_name = "find:crm.contract.payment.schedules"
	_view_name = "crm.contract.payment.schedules/find"
	_description = "Crm Contract Payment Schedules"

class ViewModelO2MFormCrmContractPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.payment.schedules"
	_view_name = "crm.contract.payment.schedules/o2m-form"
	_description = "Crm Contract Payment Schedules"

class ViewModelO2MListCrmContractPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.payment.schedules"
	_view_name = "crm.contract.payment.schedules/o2m-list"
	_description = "Crm Contract Payment Schedules"
