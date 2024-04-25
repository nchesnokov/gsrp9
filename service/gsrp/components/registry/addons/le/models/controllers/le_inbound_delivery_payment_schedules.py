from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryPaymentSchedules(ViewModelFindController):
	_name = "find:le.inbound.delivery.payment.schedules"
	_view_name = "le.inbound.delivery.payment.schedules/find"
	_description = "Inbound Delivery Payment Schedules"

class ViewModelO2MFormLeInboundDeliveryPaymentSchedules(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.payment.schedules"
	_view_name = "le.inbound.delivery.payment.schedules/o2m-form"
	_description = "Inbound Delivery Payment Schedules"

class ViewModelO2MListLeInboundDeliveryPaymentSchedules(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.payment.schedules"
	_view_name = "le.inbound.delivery.payment.schedules/o2m-list"
	_description = "Inbound Delivery Payment Schedules"
