from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjTeams(ViewModelSearchController):
	_name = "search:prj.teams"
	_view_name = "prj.teams/search"
	_description = "Project Teams"

class ViewModelFindPrjTeams(ViewModelFindController):
	_name = "find:prj.teams"
	_view_name = "prj.teams/find"
	_description = "Project Teams"

class ViewModelListPrjTeams(ViewModelListController):
	_name = "list:prj.teams"
	_view_name = "prj.teams/list"
	_description = "Project Teams"

class ViewModelFormModalPrjTeams(ViewModelFormModalController):
	_name = "form.modal:prj.teams"
	_view_name = "prj.teams/form.modal"
	_description = "Project Teams"

class ViewModelFormPrjTeams(ViewModelFormController):
	_name = "form:prj.teams"
	_view_name = "prj.teams/form"
	_description = "Project Teams"
