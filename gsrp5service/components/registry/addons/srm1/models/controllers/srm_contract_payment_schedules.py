from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractPaymentSchedules(ViewModelFindController):
	_name = "find:srm.contract.payment.schedules"
	_view_name = "srm.contract.payment.schedules/find"
	_description = "SRM Contract Payment Schedules"

class ViewModelO2MFormSrmContractPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.payment.schedules"
	_view_name = "srm.contract.payment.schedules/o2m-form"
	_description = "SRM Contract Payment Schedules"

class ViewModelO2MListSrmContractPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.payment.schedules"
	_view_name = "srm.contract.payment.schedules/o2m-list"
	_description = "SRM Contract Payment Schedules"
