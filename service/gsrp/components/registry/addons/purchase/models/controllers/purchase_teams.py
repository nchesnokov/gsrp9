from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseTeams(ViewModelSearchController):
	_name = "search:purchase.teams"
	_view_name = "purchase.teams/search"
	_description = "Purchase Teams"

class ViewModelFindPurchaseTeams(ViewModelFindController):
	_name = "find:purchase.teams"
	_view_name = "purchase.teams/find"
	_description = "Purchase Teams"

class ViewModelListPurchaseTeams(ViewModelListController):
	_name = "list:purchase.teams"
	_view_name = "purchase.teams/list"
	_description = "Purchase Teams"

class ViewModelFormModalPurchaseTeams(ViewModelFormModalController):
	_name = "form.modal:purchase.teams"
	_view_name = "purchase.teams/form.modal"
	_description = "Purchase Teams"

class ViewModelFormPurchaseTeams(ViewModelFormController):
	_name = "form:purchase.teams"
	_view_name = "purchase.teams/form"
	_description = "Purchase Teams"
