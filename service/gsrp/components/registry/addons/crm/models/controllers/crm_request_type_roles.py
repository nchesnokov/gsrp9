from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestTypeRoles(ViewModelFindController):
	_name = "find:crm.request.type.roles"
	_view_name = "crm.request.type.roles/find"
	_description = "Role CRM Request Types"

class ViewModelO2MFormCrmRequestTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.type.roles"
	_view_name = "crm.request.type.roles/o2m-form"
	_description = "Role CRM Request Types"

class ViewModelO2MListCrmRequestTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:crm.request.type.roles"
	_view_name = "crm.request.type.roles/o2m-list"
	_description = "Role CRM Request Types"
