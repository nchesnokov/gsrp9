from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFmCurrencyExchanges(ViewModelSearchController):
	_name = "search:fm.currency.exchanges"
	_view_name = "fm.currency.exchanges/search"
	_description = "Currency Exchange"

class ViewModelFindFmCurrencyExchanges(ViewModelFindController):
	_name = "find:fm.currency.exchanges"
	_view_name = "fm.currency.exchanges/find"
	_description = "Currency Exchange"

class ViewModelListFmCurrencyExchanges(ViewModelListController):
	_name = "list:fm.currency.exchanges"
	_view_name = "fm.currency.exchanges/list"
	_description = "Currency Exchange"

class ViewModelFormModalFmCurrencyExchanges(ViewModelFormModalController):
	_name = "form.modal:fm.currency.exchanges"
	_view_name = "fm.currency.exchanges/form.modal"
	_description = "Currency Exchange"

class ViewModelFormFmCurrencyExchanges(ViewModelFormController):
	_name = "form:fm.currency.exchanges"
	_view_name = "fm.currency.exchanges/form"
	_description = "Currency Exchange"
