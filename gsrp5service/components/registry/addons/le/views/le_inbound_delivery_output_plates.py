from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryOutputPlates(ViewModelFind):
	_name = "model.find.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelListLeInboundDeliveryOutputPlates(ViewModelList):
	_name = "model.list.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelFormModalLeInboundDeliveryOutputPlates(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelFormLeInboundDeliveryOutputPlates(ViewModelForm):
	_name = "model.form.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MFormLeInboundDeliveryOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelKanbanLeInboundDeliveryOutputPlates(ViewModelKanban):
	_name = "model.kanban.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MKanbanLeInboundDeliveryOutputPlates(ViewModelO2MKanban):
	_name = "model.o2mkanban.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListLeInboundDeliveryOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.output.plates"
	_model = "le.inbound.delivery.output.plates"
	_description = "Inbound Delivery Output Plates"
	_columns = ['delivery_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']
