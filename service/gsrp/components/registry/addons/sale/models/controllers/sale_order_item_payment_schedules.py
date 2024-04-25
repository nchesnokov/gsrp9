from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderItemPaymentSchedules(ViewModelFindController):
	_name = "find:sale.order.item.payment.schedules"
	_view_name = "sale.order.item.payment.schedules/find"
	_description = "Sale Order Item Payment Schedules"

class ViewModelO2MFormSaleOrderItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.item.payment.schedules"
	_view_name = "sale.order.item.payment.schedules/o2m-form"
	_description = "Sale Order Item Payment Schedules"

class ViewModelO2MListSaleOrderItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:sale.order.item.payment.schedules"
	_view_name = "sale.order.item.payment.schedules/o2m-list"
	_description = "Sale Order Item Payment Schedules"
