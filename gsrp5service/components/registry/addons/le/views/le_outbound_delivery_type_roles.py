from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeOutboundDeliveryTypeRoles(ViewModelFind):
	_name = "model.find.le.outbound.delivery.type.roles"
	_model = "le.outbound.delivery.type.roles"
	_description = "Role Outbound Delivery Types"
	_columns = ['type_id', 'role_id']

class ViewModelListLeOutboundDeliveryTypeRoles(ViewModelList):
	_name = "model.list.le.outbound.delivery.type.roles"
	_model = "le.outbound.delivery.type.roles"
	_description = "Role Outbound Delivery Types"
	_columns = ['type_id', 'role_id']

class ViewModelFormModalLeOutboundDeliveryTypeRoles(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.type.roles"
	_model = "le.outbound.delivery.type.roles"
	_description = "Role Outbound Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelFormLeOutboundDeliveryTypeRoles(ViewModelForm):
	_name = "model.form.le.outbound.delivery.type.roles"
	_model = "le.outbound.delivery.type.roles"
	_description = "Role Outbound Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MFormLeOutboundDeliveryTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.type.roles"
	_model = "le.outbound.delivery.type.roles"
	_description = "Role Outbound Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MListLeOutboundDeliveryTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.type.roles"
	_model = "le.outbound.delivery.type.roles"
	_description = "Role Outbound Delivery Types"
	_columns = ['type_id', 'role_id']
