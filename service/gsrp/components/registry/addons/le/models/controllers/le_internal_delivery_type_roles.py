from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInternalDeliveryTypeRoles(ViewModelFindController):
	_name = "find:le.internal.delivery.type.roles"
	_view_name = "le.internal.delivery.type.roles/find"
	_description = "Role Internal Delivery Types"

class ViewModelO2MFormLeInternalDeliveryTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:le.internal.delivery.type.roles"
	_view_name = "le.internal.delivery.type.roles/o2m-form"
	_description = "Role Internal Delivery Types"

class ViewModelO2MListLeInternalDeliveryTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:le.internal.delivery.type.roles"
	_view_name = "le.internal.delivery.type.roles/o2m-list"
	_description = "Role Internal Delivery Types"
