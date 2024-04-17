from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmContractItemPaymentSchedules(ViewModelFindController):
	_name = "find:crm.contract.item.payment.schedules"
	_view_name = "crm.contract.item.payment.schedules/find"
	_description = "Crm Contract Item Payment Schedules"

class ViewModelO2MFormCrmContractItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.contract.item.payment.schedules"
	_view_name = "crm.contract.item.payment.schedules/o2m-form"
	_description = "Crm Contract Item Payment Schedules"

class ViewModelO2MListCrmContractItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.contract.item.payment.schedules"
	_view_name = "crm.contract.item.payment.schedules/o2m-list"
	_description = "Crm Contract Item Payment Schedules"
