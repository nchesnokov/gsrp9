from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmAreas(ViewModelSearchController):
	_name = "search:crm.areas"
	_view_name = "crm.areas/search"
	_description = "CRM Areas"

class ViewModelFindCrmAreas(ViewModelFindController):
	_name = "find:crm.areas"
	_view_name = "crm.areas/find"
	_description = "CRM Areas"

class ViewModelListCrmAreas(ViewModelListController):
	_name = "list:crm.areas"
	_view_name = "crm.areas/list"
	_description = "CRM Areas"

class ViewModelFormModalCrmAreas(ViewModelFormModalController):
	_name = "form.modal:crm.areas"
	_view_name = "crm.areas/form.modal"
	_description = "CRM Areas"

class ViewModelFormCrmAreas(ViewModelFormController):
	_name = "form:crm.areas"
	_view_name = "crm.areas/form"
	_description = "CRM Areas"
