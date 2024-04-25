from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMdKeyCurrencies(ViewModelSearchController):
	_name = "search:md.key.currencies"
	_view_name = "md.key.currencies/search"
	_description = "Currencies Key"

class ViewModelFindMdKeyCurrencies(ViewModelFindController):
	_name = "find:md.key.currencies"
	_view_name = "md.key.currencies/find"
	_description = "Currencies Key"

class ViewModelListMdKeyCurrencies(ViewModelListController):
	_name = "list:md.key.currencies"
	_view_name = "md.key.currencies/list"
	_description = "Currencies Key"

class ViewModelFormModalMdKeyCurrencies(ViewModelFormModalController):
	_name = "form.modal:md.key.currencies"
	_view_name = "md.key.currencies/form.modal"
	_description = "Currencies Key"

class ViewModelFormMdKeyCurrencies(ViewModelFormController):
	_name = "form:md.key.currencies"
	_view_name = "md.key.currencies/form"
	_description = "Currencies Key"
