from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdCurrency(ViewModelSearchController):
	_name = "search:md.currency"
	_view_name = "md.currency/search"
	_description = "Currency"

class ViewModelFindMdCurrency(ViewModelFindController):
	_name = "find:md.currency"
	_view_name = "md.currency/find"
	_description = "Currency"

class ViewModelListMdCurrency(ViewModelListController):
	_name = "list:md.currency"
	_view_name = "md.currency/list"
	_description = "Currency"

class ViewModelFormModalMdCurrency(ViewModelFormModalController):
	_name = "form.modal:md.currency"
	_view_name = "md.currency/form.modal"
	_description = "Currency"

class ViewModelFormMdCurrency(ViewModelFormController):
	_name = "form:md.currency"
	_view_name = "md.currency/form"
	_description = "Currency"
