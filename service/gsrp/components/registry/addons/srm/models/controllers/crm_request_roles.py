from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestRoles(ViewModelFindController):
	_name = "find:crm.request.roles"
	_view_name = "crm.request.roles/find"
	_description = "CRM Request Roles"

class ViewModelO2MFormCrmRequestRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.roles"
	_view_name = "crm.request.roles/o2m-form"
	_description = "CRM Request Roles"

class ViewModelO2MListCrmRequestRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.request.roles"
	_view_name = "crm.request.roles/o2m-list"
	_description = "CRM Request Roles"
