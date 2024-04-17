from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderItemRoles(ViewModelFindController):
	_name = "find:crm.order.item.roles"
	_view_name = "crm.order.item.roles/find"
	_description = "CRM Order Roles"

class ViewModelO2MFormCrmOrderItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.item.roles"
	_view_name = "crm.order.item.roles/o2m-form"
	_description = "CRM Order Roles"

class ViewModelO2MListCrmOrderItemRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.order.item.roles"
	_view_name = "crm.order.item.roles/o2m-list"
	_description = "CRM Order Roles"
