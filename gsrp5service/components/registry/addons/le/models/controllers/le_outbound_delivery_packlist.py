from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeOutboundDeliveryPacklist(ViewModelFindController):
	_name = "find:le.outbound.delivery.packlist"
	_view_name = "le.outbound.delivery.packlist/find"
	_description = "Packlist Of Outbound Delivery"

class ViewModelO2MFormLeOutboundDeliveryPacklist(ViewModelO2MFormController):
	_name = "o2m-form:le.outbound.delivery.packlist"
	_view_name = "le.outbound.delivery.packlist/o2m-form"
	_description = "Packlist Of Outbound Delivery"

class ViewModelO2MListLeOutboundDeliveryPacklist(ViewModelO2MListController):
	_name = "o2m-list:le.outbound.delivery.packlist"
	_view_name = "le.outbound.delivery.packlist/o2m-list"
	_description = "Packlist Of Outbound Delivery"
