from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderRoles(ViewModelFindController):
	_name = "find:crm.order.roles"
	_view_name = "crm.order.roles/find"
	_description = "CRM Order Roles"

class ViewModelO2MFormCrmOrderRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.roles"
	_view_name = "crm.order.roles/o2m-form"
	_description = "CRM Order Roles"

class ViewModelO2MListCrmOrderRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.order.roles"
	_view_name = "crm.order.roles/o2m-list"
	_description = "CRM Order Roles"
