from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderPaymentSchedules(ViewModelFindController):
	_name = "find:sale.order.payment.schedules"
	_view_name = "sale.order.payment.schedules/find"
	_description = "Sale Order Payment Schedules"

class ViewModelO2MFormSaleOrderPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.payment.schedules"
	_view_name = "sale.order.payment.schedules/o2m-form"
	_description = "Sale Order Payment Schedules"

class ViewModelO2MListSaleOrderPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:sale.order.payment.schedules"
	_view_name = "sale.order.payment.schedules/o2m-list"
	_description = "Sale Order Payment Schedules"
