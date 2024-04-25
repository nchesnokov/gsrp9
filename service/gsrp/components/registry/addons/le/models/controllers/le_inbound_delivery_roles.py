from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryRoles(ViewModelFindController):
	_name = "find:le.inbound.delivery.roles"
	_view_name = "le.inbound.delivery.roles/find"
	_description = "Inbound Delivery Roles"

class ViewModelO2MFormLeInboundDeliveryRoles(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.roles"
	_view_name = "le.inbound.delivery.roles/o2m-form"
	_description = "Inbound Delivery Roles"

class ViewModelO2MListLeInboundDeliveryRoles(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.roles"
	_view_name = "le.inbound.delivery.roles/o2m-list"
	_description = "Inbound Delivery Roles"
