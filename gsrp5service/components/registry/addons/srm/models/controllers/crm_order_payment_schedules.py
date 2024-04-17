from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderPaymentSchedules(ViewModelFindController):
	_name = "find:crm.order.payment.schedules"
	_view_name = "crm.order.payment.schedules/find"
	_description = "CRM Order Payment Schedules"

class ViewModelO2MFormCrmOrderPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.payment.schedules"
	_view_name = "crm.order.payment.schedules/o2m-form"
	_description = "CRM Order Payment Schedules"

class ViewModelO2MListCrmOrderPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.order.payment.schedules"
	_view_name = "crm.order.payment.schedules/o2m-list"
	_description = "CRM Order Payment Schedules"
