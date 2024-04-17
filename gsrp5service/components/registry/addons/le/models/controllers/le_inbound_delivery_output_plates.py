from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MKanbanController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryOutputPlates(ViewModelFindController):
	_name = "find:le.inbound.delivery.output.plates"
	_view_name = "le.inbound.delivery.output.plates/find"
	_description = "Inbound Delivery Output Plates"

class ViewModelO2MFormLeInboundDeliveryOutputPlates(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.output.plates"
	_view_name = "le.inbound.delivery.output.plates/o2m-form"
	_description = "Inbound Delivery Output Plates"

class ViewModelO2MKanbanLeInboundDeliveryOutputPlates(ViewModelO2MKanbanController):
	_name = "o2m-kanban:le.inbound.delivery.output.plates"
	_view_name = "le.inbound.delivery.output.plates/o2m-kanban"
	_description = "Inbound Delivery Output Plates"

class ViewModelO2MListLeInboundDeliveryOutputPlates(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.output.plates"
	_view_name = "le.inbound.delivery.output.plates/o2m-list"
	_description = "Inbound Delivery Output Plates"
