from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryPricing(ViewModelFind):
	_name = "model.find.le.inbound.delivery.pricing"
	_model = "le.inbound.delivery.pricing"
	_description = "Inbound Delivery Pricing"
	_columns = ['delivery_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelListLeInboundDeliveryPricing(ViewModelList):
	_name = "model.list.le.inbound.delivery.pricing"
	_model = "le.inbound.delivery.pricing"
	_description = "Inbound Delivery Pricing"
	_columns = ['delivery_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelFormModalLeInboundDeliveryPricing(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.pricing"
	_model = "le.inbound.delivery.pricing"
	_description = "Inbound Delivery Pricing"
	_columns = ['delivery_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelFormLeInboundDeliveryPricing(ViewModelForm):
	_name = "model.form.le.inbound.delivery.pricing"
	_model = "le.inbound.delivery.pricing"
	_description = "Inbound Delivery Pricing"
	_columns = ['delivery_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MFormLeInboundDeliveryPricing(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.pricing"
	_model = "le.inbound.delivery.pricing"
	_description = "Inbound Delivery Pricing"
	_columns = ['delivery_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']

class ViewModelO2MListLeInboundDeliveryPricing(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.pricing"
	_model = "le.inbound.delivery.pricing"
	_description = "Inbound Delivery Pricing"
	_columns = ['delivery_id', 'level', 'cond', 'from_level', 'to_level', 'group_level', 'amount', 'currency']
