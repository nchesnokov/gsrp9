from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInboundDeliveryTypeRoles(ViewModelFindController):
	_name = "find:le.inbound.delivery.type.roles"
	_view_name = "le.inbound.delivery.type.roles/find"
	_description = "Role Inbound Delivery Types"

class ViewModelO2MFormLeInboundDeliveryTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:le.inbound.delivery.type.roles"
	_view_name = "le.inbound.delivery.type.roles/o2m-form"
	_description = "Role Inbound Delivery Types"

class ViewModelO2MListLeInboundDeliveryTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:le.inbound.delivery.type.roles"
	_view_name = "le.inbound.delivery.type.roles/o2m-list"
	_description = "Role Inbound Delivery Types"
