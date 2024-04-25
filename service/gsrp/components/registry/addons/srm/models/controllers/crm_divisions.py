from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmDivisions(ViewModelSearchController):
	_name = "search:crm.divisions"
	_view_name = "crm.divisions/search"
	_description = "CRM Divisions"

class ViewModelFindCrmDivisions(ViewModelFindController):
	_name = "find:crm.divisions"
	_view_name = "crm.divisions/find"
	_description = "CRM Divisions"

class ViewModelListCrmDivisions(ViewModelListController):
	_name = "list:crm.divisions"
	_view_name = "crm.divisions/list"
	_description = "CRM Divisions"

class ViewModelFormModalCrmDivisions(ViewModelFormModalController):
	_name = "form.modal:crm.divisions"
	_view_name = "crm.divisions/form.modal"
	_description = "CRM Divisions"

class ViewModelFormCrmDivisions(ViewModelFormController):
	_name = "form:crm.divisions"
	_view_name = "crm.divisions/form"
	_description = "CRM Divisions"
