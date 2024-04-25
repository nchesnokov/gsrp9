from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountsTaxGroup(ViewModelSearchController):
	_name = "search:fa.accounts.tax.group"
	_view_name = "fa.accounts.tax.group/search"
	_description = "General Model Account Tax Group"

class ViewModelFindFaAccountsTaxGroup(ViewModelFindController):
	_name = "find:fa.accounts.tax.group"
	_view_name = "fa.accounts.tax.group/find"
	_description = "General Model Account Tax Group"

class ViewModelListFaAccountsTaxGroup(ViewModelListController):
	_name = "list:fa.accounts.tax.group"
	_view_name = "fa.accounts.tax.group/list"
	_description = "General Model Account Tax Group"

class ViewModelFormModalFaAccountsTaxGroup(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.tax.group"
	_view_name = "fa.accounts.tax.group/form.modal"
	_description = "General Model Account Tax Group"

class ViewModelFormFaAccountsTaxGroup(ViewModelFormController):
	_name = "form:fa.accounts.tax.group"
	_view_name = "fa.accounts.tax.group/form"
	_description = "General Model Account Tax Group"
