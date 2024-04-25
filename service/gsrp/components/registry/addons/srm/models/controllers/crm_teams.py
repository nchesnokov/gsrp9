from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmTeams(ViewModelSearchController):
	_name = "search:crm.teams"
	_view_name = "crm.teams/search"
	_description = "CRM Teams"

class ViewModelFindCrmTeams(ViewModelFindController):
	_name = "find:crm.teams"
	_view_name = "crm.teams/find"
	_description = "CRM Teams"

class ViewModelListCrmTeams(ViewModelListController):
	_name = "list:crm.teams"
	_view_name = "crm.teams/list"
	_description = "CRM Teams"

class ViewModelFormModalCrmTeams(ViewModelFormModalController):
	_name = "form.modal:crm.teams"
	_view_name = "crm.teams/form.modal"
	_description = "CRM Teams"

class ViewModelFormCrmTeams(ViewModelFormController):
	_name = "form:crm.teams"
	_view_name = "crm.teams/form"
	_description = "CRM Teams"
