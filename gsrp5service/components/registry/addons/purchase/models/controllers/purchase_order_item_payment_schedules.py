from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderItemPaymentSchedules(ViewModelFindController):
	_name = "find:purchase.order.item.payment.schedules"
	_view_name = "purchase.order.item.payment.schedules/find"
	_description = "Purchase Order Item Payment Schedules"

class ViewModelO2MFormPurchaseOrderItemPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.item.payment.schedules"
	_view_name = "purchase.order.item.payment.schedules/o2m-form"
	_description = "Purchase Order Item Payment Schedules"

class ViewModelO2MListPurchaseOrderItemPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.item.payment.schedules"
	_view_name = "purchase.order.item.payment.schedules/o2m-list"
	_description = "Purchase Order Item Payment Schedules"
