from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryRoles(ViewModelFind):
	_name = "model.find.le.inbound.delivery.roles"
	_model = "le.inbound.delivery.roles"
	_description = "Inbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelListLeInboundDeliveryRoles(ViewModelList):
	_name = "model.list.le.inbound.delivery.roles"
	_model = "le.inbound.delivery.roles"
	_description = "Inbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelFormModalLeInboundDeliveryRoles(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.roles"
	_model = "le.inbound.delivery.roles"
	_description = "Inbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelFormLeInboundDeliveryRoles(ViewModelForm):
	_name = "model.form.le.inbound.delivery.roles"
	_model = "le.inbound.delivery.roles"
	_description = "Inbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelO2MFormLeInboundDeliveryRoles(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.roles"
	_model = "le.inbound.delivery.roles"
	_description = "Inbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelO2MListLeInboundDeliveryRoles(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.roles"
	_model = "le.inbound.delivery.roles"
	_description = "Inbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']
