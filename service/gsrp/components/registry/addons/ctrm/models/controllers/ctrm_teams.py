from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCtrmTeams(ViewModelSearchController):
	_name = "search:ctrm.teams"
	_view_name = "ctrm.teams/search"
	_description = "CTRM Teams"

class ViewModelFindCtrmTeams(ViewModelFindController):
	_name = "find:ctrm.teams"
	_view_name = "ctrm.teams/find"
	_description = "CTRM Teams"

class ViewModelListCtrmTeams(ViewModelListController):
	_name = "list:ctrm.teams"
	_view_name = "ctrm.teams/list"
	_description = "CTRM Teams"

class ViewModelFormModalCtrmTeams(ViewModelFormModalController):
	_name = "form.modal:ctrm.teams"
	_view_name = "ctrm.teams/form.modal"
	_description = "CTRM Teams"

class ViewModelFormCtrmTeams(ViewModelFormController):
	_name = "form:ctrm.teams"
	_view_name = "ctrm.teams/form"
	_description = "CTRM Teams"
