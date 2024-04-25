from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeInboundDeliveryTypes(ViewModelSearch):
	_name = "model.search.le.inbound.delivery.types"
	_model = "le.inbound.delivery.types"
	_description = "Types Inbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'required']

class ViewModelFindLeInboundDeliveryTypes(ViewModelFind):
	_name = "model.find.le.inbound.delivery.types"
	_model = "le.inbound.delivery.types"
	_description = "Types Inbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'required']

class ViewModelListLeInboundDeliveryTypes(ViewModelList):
	_name = "model.list.le.inbound.delivery.types"
	_model = "le.inbound.delivery.types"
	_description = "Types Inbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required']

class ViewModelFormModalLeInboundDeliveryTypes(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.types"
	_model = "le.inbound.delivery.types"
	_description = "Types Inbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelFormLeInboundDeliveryTypes(ViewModelForm):
	_name = "model.form.le.inbound.delivery.types"
	_model = "le.inbound.delivery.types"
	_description = "Types Inbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelO2MFormLeInboundDeliveryTypes(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.types"
	_model = "le.inbound.delivery.types"
	_description = "Types Inbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelO2MListLeInboundDeliveryTypes(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.types"
	_model = "le.inbound.delivery.types"
	_description = "Types Inbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required']
