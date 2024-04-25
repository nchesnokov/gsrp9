from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleMarkets(ViewModelSearchController):
	_name = "search:sale.markets"
	_view_name = "sale.markets/search"
	_description = "Sale Market"

class ViewModelFindSaleMarkets(ViewModelFindController):
	_name = "find:sale.markets"
	_view_name = "sale.markets/find"
	_description = "Sale Market"

class ViewModelListSaleMarkets(ViewModelListController):
	_name = "list:sale.markets"
	_view_name = "sale.markets/list"
	_description = "Sale Market"

class ViewModelFormModalSaleMarkets(ViewModelFormModalController):
	_name = "form.modal:sale.markets"
	_view_name = "sale.markets/form.modal"
	_description = "Sale Market"

class ViewModelFormSaleMarkets(ViewModelFormController):
	_name = "form:sale.markets"
	_view_name = "sale.markets/form"
	_description = "Sale Market"
