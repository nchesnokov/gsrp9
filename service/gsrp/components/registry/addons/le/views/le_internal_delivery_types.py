from gsrp5service.obj.view import ViewModelSearch
from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelSearchLeInternalDeliveryTypes(ViewModelSearch):
	_name = "model.search.le.internal.delivery.types"
	_model = "le.internal.delivery.types"
	_description = "Types Internal Delivery"
	_columns = ['name', 'htschema', 'itschema', 'required']

class ViewModelFindLeInternalDeliveryTypes(ViewModelFind):
	_name = "model.find.le.internal.delivery.types"
	_model = "le.internal.delivery.types"
	_description = "Types Internal Delivery"
	_columns = ['name', 'htschema', 'itschema', 'required']

class ViewModelListLeInternalDeliveryTypes(ViewModelList):
	_name = "model.list.le.internal.delivery.types"
	_model = "le.internal.delivery.types"
	_description = "Types Internal Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required']

class ViewModelFormModalLeInternalDeliveryTypes(ViewModelFormModal):
	_name = "model.form.modal.le.internal.delivery.types"
	_model = "le.internal.delivery.types"
	_description = "Types Internal Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelFormLeInternalDeliveryTypes(ViewModelForm):
	_name = "model.form.le.internal.delivery.types"
	_model = "le.internal.delivery.types"
	_description = "Types Internal Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelO2MFormLeInternalDeliveryTypes(ViewModelO2MForm):
	_name = "model.o2mform.le.internal.delivery.types"
	_model = "le.internal.delivery.types"
	_description = "Types Internal Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required', 'note']

class ViewModelO2MListLeInternalDeliveryTypes(ViewModelO2MList):
	_name = "model.o2mlist.le.internal.delivery.types"
	_model = "le.internal.delivery.types"
	_description = "Types Internal Delivery"
	_columns = ['name', 'htschema', 'itschema', 'roles', 'required']
