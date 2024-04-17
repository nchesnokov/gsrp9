from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmMarkets(ViewModelSearchController):
	_name = "search:srm.markets"
	_view_name = "srm.markets/search"
	_description = "SRM Market"

class ViewModelFindSrmMarkets(ViewModelFindController):
	_name = "find:srm.markets"
	_view_name = "srm.markets/find"
	_description = "SRM Market"

class ViewModelListSrmMarkets(ViewModelListController):
	_name = "list:srm.markets"
	_view_name = "srm.markets/list"
	_description = "SRM Market"

class ViewModelFormModalSrmMarkets(ViewModelFormModalController):
	_name = "form.modal:srm.markets"
	_view_name = "srm.markets/form.modal"
	_description = "SRM Market"

class ViewModelFormSrmMarkets(ViewModelFormController):
	_name = "form:srm.markets"
	_view_name = "srm.markets/form"
	_description = "SRM Market"
