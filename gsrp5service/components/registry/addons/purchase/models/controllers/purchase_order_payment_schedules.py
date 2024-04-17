from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderPaymentSchedules(ViewModelFindController):
	_name = "find:purchase.order.payment.schedules"
	_view_name = "purchase.order.payment.schedules/find"
	_description = "Purchase Order Payment Schedules"

class ViewModelO2MFormPurchaseOrderPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.payment.schedules"
	_view_name = "purchase.order.payment.schedules/o2m-form"
	_description = "Purchase Order Payment Schedules"

class ViewModelO2MListPurchaseOrderPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.payment.schedules"
	_view_name = "purchase.order.payment.schedules/o2m-list"
	_description = "Purchase Order Payment Schedules"
