from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindLeInternalDeliveryRoles(ViewModelFindController):
	_name = "find:le.internal.delivery.roles"
	_view_name = "le.internal.delivery.roles/find"
	_description = "Internal Delivery Roles"

class ViewModelO2MFormLeInternalDeliveryRoles(ViewModelO2MFormController):
	_name = "o2m-form:le.internal.delivery.roles"
	_view_name = "le.internal.delivery.roles/o2m-form"
	_description = "Internal Delivery Roles"

class ViewModelO2MListLeInternalDeliveryRoles(ViewModelO2MListController):
	_name = "o2m-list:le.internal.delivery.roles"
	_view_name = "le.internal.delivery.roles/o2m-list"
	_description = "Internal Delivery Roles"
