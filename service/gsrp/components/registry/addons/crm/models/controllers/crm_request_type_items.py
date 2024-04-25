from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestTypeItems(ViewModelFindController):
	_name = "find:crm.request.type.items"
	_view_name = "crm.request.type.items/find"
	_description = "Role CRM Request Items"

class ViewModelO2MFormCrmRequestTypeItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.type.items"
	_view_name = "crm.request.type.items/o2m-form"
	_description = "Role CRM Request Items"

class ViewModelO2MListCrmRequestTypeItems(ViewModelO2MListController):
	_name = "o2m-list:crm.request.type.items"
	_view_name = "crm.request.type.items/o2m-list"
	_description = "Role CRM Request Items"
