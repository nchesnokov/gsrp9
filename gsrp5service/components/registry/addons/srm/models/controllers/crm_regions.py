from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmRegions(ViewModelSearchController):
	_name = "search:crm.regions"
	_view_name = "crm.regions/search"
	_description = "CRM Regions"

class ViewModelFindCrmRegions(ViewModelFindController):
	_name = "find:crm.regions"
	_view_name = "crm.regions/find"
	_description = "CRM Regions"

class ViewModelListCrmRegions(ViewModelListController):
	_name = "list:crm.regions"
	_view_name = "crm.regions/list"
	_description = "CRM Regions"

class ViewModelFormModalCrmRegions(ViewModelFormModalController):
	_name = "form.modal:crm.regions"
	_view_name = "crm.regions/form.modal"
	_description = "CRM Regions"

class ViewModelFormCrmRegions(ViewModelFormController):
	_name = "form:crm.regions"
	_view_name = "crm.regions/form"
	_description = "CRM Regions"
