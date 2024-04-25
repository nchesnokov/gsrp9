from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestItemRoles(ViewModelFindController):
	_name = "find:crm.request.item.roles"
	_view_name = "crm.request.item.roles/find"
	_description = "CRM Request Roles"

class ViewModelO2MFormCrmRequestItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.item.roles"
	_view_name = "crm.request.item.roles/o2m-form"
	_description = "CRM Request Roles"

class ViewModelO2MListCrmRequestItemRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.request.item.roles"
	_view_name = "crm.request.item.roles/o2m-list"
	_description = "CRM Request Roles"
