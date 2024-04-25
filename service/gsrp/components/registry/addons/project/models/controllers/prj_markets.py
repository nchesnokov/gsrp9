from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjMarkets(ViewModelSearchController):
	_name = "search:prj.markets"
	_view_name = "prj.markets/search"
	_description = "Project Market"

class ViewModelFindPrjMarkets(ViewModelFindController):
	_name = "find:prj.markets"
	_view_name = "prj.markets/find"
	_description = "Project Market"

class ViewModelListPrjMarkets(ViewModelListController):
	_name = "list:prj.markets"
	_view_name = "prj.markets/list"
	_description = "Project Market"

class ViewModelFormModalPrjMarkets(ViewModelFormModalController):
	_name = "form.modal:prj.markets"
	_view_name = "prj.markets/form.modal"
	_description = "Project Market"

class ViewModelFormPrjMarkets(ViewModelFormController):
	_name = "form:prj.markets"
	_view_name = "prj.markets/form"
	_description = "Project Market"
