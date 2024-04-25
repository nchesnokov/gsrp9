from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderItemPaymentSchedules(ViewModelFindController):
	_name = "find:crm.order.item.payment.schedules"
	_view_name = "crm.order.item.payment.schedules/find"
	_description = "CRM Order Item Payment Schedules"

class ViewModelO2MFormCrmOrderItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.item.payment.schedules"
	_view_name = "crm.order.item.payment.schedules/o2m-form"
	_description = "CRM Order Item Payment Schedules"

class ViewModelO2MListCrmOrderItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:crm.order.item.payment.schedules"
	_view_name = "crm.order.item.payment.schedules/o2m-list"
	_description = "CRM Order Item Payment Schedules"
