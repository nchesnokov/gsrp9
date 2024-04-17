from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInternalDeliveryPacklist(ViewModelFindController):
	_name = "find:le.internal.delivery.packlist"
	_view_name = "le.internal.delivery.packlist/find"
	_description = "Packlist Of Internal Delivery"

class ViewModelO2MFormLeInternalDeliveryPacklist(ViewModelO2MFormController):
	_name = "o2m-form:le.internal.delivery.packlist"
	_view_name = "le.internal.delivery.packlist/o2m-form"
	_description = "Packlist Of Internal Delivery"

class ViewModelO2MListLeInternalDeliveryPacklist(ViewModelO2MListController):
	_name = "o2m-list:le.internal.delivery.packlist"
	_view_name = "le.internal.delivery.packlist/o2m-list"
	_description = "Packlist Of Internal Delivery"
