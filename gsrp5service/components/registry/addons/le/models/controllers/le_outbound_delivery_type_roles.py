from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeOutboundDeliveryTypeRoles(ViewModelFindController):
	_name = "find:le.outbound.delivery.type.roles"
	_view_name = "le.outbound.delivery.type.roles/find"
	_description = "Role Outbound Delivery Types"

class ViewModelO2MFormLeOutboundDeliveryTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:le.outbound.delivery.type.roles"
	_view_name = "le.outbound.delivery.type.roles/o2m-form"
	_description = "Role Outbound Delivery Types"

class ViewModelO2MListLeOutboundDeliveryTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:le.outbound.delivery.type.roles"
	_view_name = "le.outbound.delivery.type.roles/o2m-list"
	_description = "Role Outbound Delivery Types"
