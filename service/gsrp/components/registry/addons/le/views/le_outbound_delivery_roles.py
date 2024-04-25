from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeOutboundDeliveryRoles(ViewModelFind):
	_name = "model.find.le.outbound.delivery.roles"
	_model = "le.outbound.delivery.roles"
	_description = "Outbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelListLeOutboundDeliveryRoles(ViewModelList):
	_name = "model.list.le.outbound.delivery.roles"
	_model = "le.outbound.delivery.roles"
	_description = "Outbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelFormModalLeOutboundDeliveryRoles(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.roles"
	_model = "le.outbound.delivery.roles"
	_description = "Outbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelFormLeOutboundDeliveryRoles(ViewModelForm):
	_name = "model.form.le.outbound.delivery.roles"
	_model = "le.outbound.delivery.roles"
	_description = "Outbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelO2MFormLeOutboundDeliveryRoles(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.roles"
	_model = "le.outbound.delivery.roles"
	_description = "Outbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelO2MListLeOutboundDeliveryRoles(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.roles"
	_model = "le.outbound.delivery.roles"
	_description = "Outbound Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']
