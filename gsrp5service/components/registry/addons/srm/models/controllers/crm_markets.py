from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmMarkets(ViewModelSearchController):
	_name = "search:crm.markets"
	_view_name = "crm.markets/search"
	_description = "CRM Market"

class ViewModelFindCrmMarkets(ViewModelFindController):
	_name = "find:crm.markets"
	_view_name = "crm.markets/find"
	_description = "CRM Market"

class ViewModelListCrmMarkets(ViewModelListController):
	_name = "list:crm.markets"
	_view_name = "crm.markets/list"
	_description = "CRM Market"

class ViewModelFormModalCrmMarkets(ViewModelFormModalController):
	_name = "form.modal:crm.markets"
	_view_name = "crm.markets/form.modal"
	_description = "CRM Market"

class ViewModelFormCrmMarkets(ViewModelFormController):
	_name = "form:crm.markets"
	_view_name = "crm.markets/form"
	_description = "CRM Market"
