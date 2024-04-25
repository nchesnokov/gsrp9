from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeOutboundDeliveryRoles(ViewModelFindController):
	_name = "find:le.outbound.delivery.roles"
	_view_name = "le.outbound.delivery.roles/find"
	_description = "Outbound Delivery Roles"

class ViewModelO2MFormLeOutboundDeliveryRoles(ViewModelO2MFormController):
	_name = "o2m-form:le.outbound.delivery.roles"
	_view_name = "le.outbound.delivery.roles/o2m-form"
	_description = "Outbound Delivery Roles"

class ViewModelO2MListLeOutboundDeliveryRoles(ViewModelO2MListController):
	_name = "o2m-list:le.outbound.delivery.roles"
	_view_name = "le.outbound.delivery.roles/o2m-list"
	_description = "Outbound Delivery Roles"
