from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryItemOutputPlates(ViewModelFindController):
	_name = "find:le.inbound.delivery.item.output.plates"
	_view_name = "le.inbound.delivery.item.output.plates/find"
	_description = "Inbound Delivery Item Output Plates"

class ViewModelO2MFormLeInboundDeliveryItemOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.item.output.plates"
	_view_name = "le.inbound.delivery.item.output.plates/o2m-form"
	_description = "Inbound Delivery Item Output Plates"

class ViewModelO2MKanbanLeInboundDeliveryItemOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:le.inbound.delivery.item.output.plates"
	_view_name = "le.inbound.delivery.item.output.plates/o2m-kanban"
	_description = "Inbound Delivery Item Output Plates"

class ViewModelO2MListLeInboundDeliveryItemOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.item.output.plates"
	_view_name = "le.inbound.delivery.item.output.plates/o2m-list"
	_description = "Inbound Delivery Item Output Plates"
