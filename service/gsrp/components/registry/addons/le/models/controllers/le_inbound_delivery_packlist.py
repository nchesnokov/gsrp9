from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryPacklist(ViewModelFindController):
	_name = "find:le.inbound.delivery.packlist"
	_view_name = "le.inbound.delivery.packlist/find"
	_description = "Packlist Of Inbound Delivery"

class ViewModelO2MFormLeInboundDeliveryPacklist(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.packlist"
	_view_name = "le.inbound.delivery.packlist/o2m-form"
	_description = "Packlist Of Inbound Delivery"

class ViewModelO2MListLeInboundDeliveryPacklist(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.packlist"
	_view_name = "le.inbound.delivery.packlist/o2m-list"
	_description = "Packlist Of Inbound Delivery"
