from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmContractItemPaymentSchedules(ViewModelFindController):
	_name = "find:srm.contract.item.payment.schedules"
	_view_name = "srm.contract.item.payment.schedules/find"
	_description = "Contract Item Payment Schedules"

class ViewModelO2MFormSrmContractItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:srm.contract.item.payment.schedules"
	_view_name = "srm.contract.item.payment.schedules/o2m-form"
	_description = "Contract Item Payment Schedules"

class ViewModelO2MListSrmContractItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:srm.contract.item.payment.schedules"
	_view_name = "srm.contract.item.payment.schedules/o2m-list"
	_description = "Contract Item Payment Schedules"
