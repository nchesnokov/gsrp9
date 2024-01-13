from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryPaymentSchedules(ViewModelFind):
	_name = "model.find.le.inbound.delivery.payment.schedules"
	_model = "le.inbound.delivery.payment.schedules"
	_description = "Inbound Delivery Payment Schedules"
	_columns = ['delivery_id', 'amount', 'currency', 'schedule']

class ViewModelListLeInboundDeliveryPaymentSchedules(ViewModelList):
	_name = "model.list.le.inbound.delivery.payment.schedules"
	_model = "le.inbound.delivery.payment.schedules"
	_description = "Inbound Delivery Payment Schedules"
	_columns = ['delivery_id', 'amount', 'currency', 'schedule']

class ViewModelFormModalLeInboundDeliveryPaymentSchedules(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.payment.schedules"
	_model = "le.inbound.delivery.payment.schedules"
	_description = "Inbound Delivery Payment Schedules"
	_columns = ['delivery_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelFormLeInboundDeliveryPaymentSchedules(ViewModelForm):
	_name = "model.form.le.inbound.delivery.payment.schedules"
	_model = "le.inbound.delivery.payment.schedules"
	_description = "Inbound Delivery Payment Schedules"
	_columns = ['delivery_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MFormLeInboundDeliveryPaymentSchedules(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.payment.schedules"
	_model = "le.inbound.delivery.payment.schedules"
	_description = "Inbound Delivery Payment Schedules"
	_columns = ['delivery_id', 'amount', 'currency', 'schedule', 'note']

class ViewModelO2MListLeInboundDeliveryPaymentSchedules(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.payment.schedules"
	_model = "le.inbound.delivery.payment.schedules"
	_description = "Inbound Delivery Payment Schedules"
	_columns = ['delivery_id', 'amount', 'currency', 'schedule']
