from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleTeams(ViewModelSearchController):
	_name = "search:sale.teams"
	_view_name = "sale.teams/search"
	_description = "Sale Teams"

class ViewModelFindSaleTeams(ViewModelFindController):
	_name = "find:sale.teams"
	_view_name = "sale.teams/find"
	_description = "Sale Teams"

class ViewModelListSaleTeams(ViewModelListController):
	_name = "list:sale.teams"
	_view_name = "sale.teams/list"
	_description = "Sale Teams"

class ViewModelFormModalSaleTeams(ViewModelFormModalController):
	_name = "form.modal:sale.teams"
	_view_name = "sale.teams/form.modal"
	_description = "Sale Teams"

class ViewModelFormSaleTeams(ViewModelFormController):
	_name = "form:sale.teams"
	_view_name = "sale.teams/form"
	_description = "Sale Teams"
