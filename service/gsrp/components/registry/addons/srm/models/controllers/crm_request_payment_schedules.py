from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestPaymentSchedules(ViewModelFindController):
	_name = "find:crm.request.payment.schedules"
	_view_name = "crm.request.payment.schedules/find"
	_description = "CRM Request Payment Schedules"

class ViewModelO2MFormCrmRequestPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.payment.schedules"
	_view_name = "crm.request.payment.schedules/o2m-form"
	_description = "CRM Request Payment Schedules"

class ViewModelO2MListCrmRequestPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.request.payment.schedules"
	_view_name = "crm.request.payment.schedules/o2m-list"
	_description = "CRM Request Payment Schedules"
