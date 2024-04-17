from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchaseMarkets(ViewModelSearchController):
	_name = "search:purchase.markets"
	_view_name = "purchase.markets/search"
	_description = "Purchase Market"

class ViewModelFindPurchaseMarkets(ViewModelFindController):
	_name = "find:purchase.markets"
	_view_name = "purchase.markets/find"
	_description = "Purchase Market"

class ViewModelListPurchaseMarkets(ViewModelListController):
	_name = "list:purchase.markets"
	_view_name = "purchase.markets/list"
	_description = "Purchase Market"

class ViewModelFormModalPurchaseMarkets(ViewModelFormModalController):
	_name = "form.modal:purchase.markets"
	_view_name = "purchase.markets/form.modal"
	_description = "Purchase Market"

class ViewModelFormPurchaseMarkets(ViewModelFormController):
	_name = "form:purchase.markets"
	_view_name = "purchase.markets/form"
	_description = "Purchase Market"
