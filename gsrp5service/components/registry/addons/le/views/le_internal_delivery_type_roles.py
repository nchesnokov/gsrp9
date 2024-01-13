from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInternalDeliveryTypeRoles(ViewModelFind):
	_name = "model.find.le.internal.delivery.type.roles"
	_model = "le.internal.delivery.type.roles"
	_description = "Role Internal Delivery Types"
	_columns = ['type_id', 'role_id']

class ViewModelListLeInternalDeliveryTypeRoles(ViewModelList):
	_name = "model.list.le.internal.delivery.type.roles"
	_model = "le.internal.delivery.type.roles"
	_description = "Role Internal Delivery Types"
	_columns = ['type_id', 'role_id']

class ViewModelFormModalLeInternalDeliveryTypeRoles(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.type.roles"
	_model = "le.internal.delivery.type.roles"
	_description = "Role Internal Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelFormLeInternalDeliveryTypeRoles(ViewModelForm):
	_name = "model.form.le.internal.delivery.type.roles"
	_model = "le.internal.delivery.type.roles"
	_description = "Role Internal Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MFormLeInternalDeliveryTypeRoles(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.type.roles"
	_model = "le.internal.delivery.type.roles"
	_description = "Role Internal Delivery Types"
	_columns = ['type_id', 'role_id', 'note']

class ViewModelO2MListLeInternalDeliveryTypeRoles(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.type.roles"
	_model = "le.internal.delivery.type.roles"
	_description = "Role Internal Delivery Types"
	_columns = ['type_id', 'role_id']
