from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountsType(ViewModelSearchController):
	_name = "search:fa.accounts.type"
	_view_name = "fa.accounts.type/search"
	_description = "Account Type"

class ViewModelFindFaAccountsType(ViewModelFindController):
	_name = "find:fa.accounts.type"
	_view_name = "fa.accounts.type/find"
	_description = "Account Type"

class ViewModelListFaAccountsType(ViewModelListController):
	_name = "list:fa.accounts.type"
	_view_name = "fa.accounts.type/list"
	_description = "Account Type"

class ViewModelFormModalFaAccountsType(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.type"
	_view_name = "fa.accounts.type/form.modal"
	_description = "Account Type"

class ViewModelFormFaAccountsType(ViewModelFormController):
	_name = "form:fa.accounts.type"
	_view_name = "fa.accounts.type/form"
	_description = "Account Type"
