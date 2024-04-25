from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestItemPaymentSchedules(ViewModelFindController):
	_name = "find:crm.request.item.payment.schedules"
	_view_name = "crm.request.item.payment.schedules/find"
	_description = "CRM Request Item Payment Schedules"

class ViewModelO2MFormCrmRequestItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.item.payment.schedules"
	_view_name = "crm.request.item.payment.schedules/o2m-form"
	_description = "CRM Request Item Payment Schedules"

class ViewModelO2MListCrmRequestItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.request.item.payment.schedules"
	_view_name = "crm.request.item.payment.schedules/o2m-list"
	_description = "CRM Request Item Payment Schedules"
