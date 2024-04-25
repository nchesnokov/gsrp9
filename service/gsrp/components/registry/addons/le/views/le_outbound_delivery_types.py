from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeOutboundDeliveryTypes(ViewModelSearch):
	_name = "model.search.le.outbound.delivery.types"
	_model = "le.outbound.delivery.types"
	_description = "Types Outbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'required']

class ViewModelFindLeOutboundDeliveryTypes(ViewModelFind):
	_name = "model.find.le.outbound.delivery.types"
	_model = "le.outbound.delivery.types"
	_description = "Types Outbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'required']

class ViewModelListLeOutboundDeliveryTypes(ViewModelList):
	_name = "model.list.le.outbound.delivery.types"
	_model = "le.outbound.delivery.types"
	_description = "Types Outbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required']

class ViewModelFormModalLeOutboundDeliveryTypes(ViewModelFormModal):
	_name = "model.form.modal.le.outbound.delivery.types"
	_model = "le.outbound.delivery.types"
	_description = "Types Outbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelFormLeOutboundDeliveryTypes(ViewModelForm):
	_name = "model.form.le.outbound.delivery.types"
	_model = "le.outbound.delivery.types"
	_description = "Types Outbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelO2MFormLeOutboundDeliveryTypes(ViewModelO2MForm):
	_name = "model.o2mform.le.outbound.delivery.types"
	_model = "le.outbound.delivery.types"
	_description = "Types Outbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelO2MListLeOutboundDeliveryTypes(ViewModelO2MList):
	_name = "model.o2mlist.le.outbound.delivery.types"
	_model = "le.outbound.delivery.types"
	_description = "Types Outbound Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required']
