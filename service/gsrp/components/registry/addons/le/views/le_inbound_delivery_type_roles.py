from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryTypeRoles(ViewModelFind):
	_name = "model.find.le.inbound.delivery.type.roles"
	_model = "le.inbound.delivery.type.roles"
	_description = "Role Inbound Delivery Types"
	_columns = ['type_id', 'role_id']

class ViewModelListLeInboundDeliveryTypeRoles(ViewModelList):
	_name = "model.list.le.inbound.delivery.type.roles"
	_model = "le.inbound.delivery.type.roles"
	_description = "Role Inbound Delivery Types"
	_columns = ['type_id', 'role_id']

class ViewModelFormModalLeInboundDeliveryTypeRoles(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.type.roles"
	_model = "le.inbound.delivery.type.roles"
	_description = "Role Inbound Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelFormLeInboundDeliveryTypeRoles(ViewModelForm):
	_name = "model.form.le.inbound.delivery.type.roles"
	_model = "le.inbound.delivery.type.roles"
	_description = "Role Inbound Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MFormLeInboundDeliveryTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.type.roles"
	_model = "le.inbound.delivery.type.roles"
	_description = "Role Inbound Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MListLeInboundDeliveryTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.type.roles"
	_model = "le.inbound.delivery.type.roles"
	_description = "Role Inbound Delivery Types"
	_columns = ['type_id', 'role_id']
