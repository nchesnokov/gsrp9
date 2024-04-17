from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestItems(ViewModelFindController):
	_name = "find:crm.request.items"
	_view_name = "crm.request.items/find"
	_description = "CRM Request Items"

class ViewModelO2MFormCrmRequestItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.items"
	_view_name = "crm.request.items/o2m-form"
	_description = "CRM Request Items"

class ViewModelO2MListCrmRequestItems(ViewModelO2MListController):
	_name = "o2m-list:crm.request.items"
	_view_name = "crm.request.items/o2m-list"
	_description = "CRM Request Items"
