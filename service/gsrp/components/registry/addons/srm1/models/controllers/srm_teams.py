from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmTeams(ViewModelSearchController):
	_name = "search:srm.teams"
	_view_name = "srm.teams/search"
	_description = "SRM Teams"

class ViewModelFindSrmTeams(ViewModelFindController):
	_name = "find:srm.teams"
	_view_name = "srm.teams/find"
	_description = "SRM Teams"

class ViewModelListSrmTeams(ViewModelListController):
	_name = "list:srm.teams"
	_view_name = "srm.teams/list"
	_description = "SRM Teams"

class ViewModelFormModalSrmTeams(ViewModelFormModalController):
	_name = "form.modal:srm.teams"
	_view_name = "srm.teams/form.modal"
	_description = "SRM Teams"

class ViewModelFormSrmTeams(ViewModelFormController):
	_name = "form:srm.teams"
	_view_name = "srm.teams/form"
	_description = "SRM Teams"
