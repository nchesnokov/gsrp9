from gsrp5service.obj.view import ViewModelFind
from gsrp5service.obj.view import ViewModelList
from gsrp5service.obj.view import ViewModelFormModal
from gsrp5service.obj.view import ViewModelForm
from gsrp5service.obj.view import ViewModelO2MForm
from gsrp5service.obj.view import ViewModelKanban
from gsrp5service.obj.view import ViewModelO2MKanban
from gsrp5service.obj.view import ViewModelO2MList

class ViewModelFindLeInboundDeliveryItemOutputPlates(ViewModelFind):
	_name = "model.find.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelListLeInboundDeliveryItemOutputPlates(ViewModelList):
	_name = "model.list.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']

class ViewModelFormModalLeInboundDeliveryItemOutputPlates(ViewModelFormModal):
	_name = "model.form.modal.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelFormLeInboundDeliveryItemOutputPlates(ViewModelForm):
	_name = "model.form.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MFormLeInboundDeliveryItemOutputPlates(ViewModelO2MForm):
	_name = "model.o2mform.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelKanbanLeInboundDeliveryItemOutputPlates(ViewModelKanban):
	_name = "model.kanban.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MKanbanLeInboundDeliveryItemOutputPlates(ViewModelO2MKanban):
	_name = "model.o2mkanban.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule', 'note']

class ViewModelO2MListLeInboundDeliveryItemOutputPlates(ViewModelO2MList):
	_name = "model.o2mlist.le.inbound.delivery.item.output.plates"
	_model = "le.inbound.delivery.item.output.plates"
	_description = "Inbound Delivery Item Output Plates"
	_columns = ['item_id', 'state', 'otype', 'partner', 'role', 'language', 'msm', 'schedule']
