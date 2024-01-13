from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInternalDeliveryRoles(ViewModelFind):
	_name = "model.find.le.internal.delivery.roles"
	_model = "le.internal.delivery.roles"
	_description = "Internal Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelListLeInternalDeliveryRoles(ViewModelList):
	_name = "model.list.le.internal.delivery.roles"
	_model = "le.internal.delivery.roles"
	_description = "Internal Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelFormModalLeInternalDeliveryRoles(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.roles"
	_model = "le.internal.delivery.roles"
	_description = "Internal Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelFormLeInternalDeliveryRoles(ViewModelForm):
	_name = "model.form.le.internal.delivery.roles"
	_model = "le.internal.delivery.roles"
	_description = "Internal Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelO2MFormLeInternalDeliveryRoles(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.roles"
	_model = "le.internal.delivery.roles"
	_description = "Internal Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']

class ViewModelO2MListLeInternalDeliveryRoles(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.roles"
	_model = "le.internal.delivery.roles"
	_description = "Internal Delivery Roles"
	_columns = ['delivery_id', 'role_id', 'patner_id']
