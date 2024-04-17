from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccounts(ViewModelSearchController):
	_name = "search:fa.accounts"
	_view_name = "fa.accounts/search"
	_description = "Genaral Model Account"

class ViewModelFindFaAccounts(ViewModelFindController):
	_name = "find:fa.accounts"
	_view_name = "fa.accounts/find"
	_description = "Genaral Model Account"

class ViewModelListFaAccounts(ViewModelListController):
	_name = "list:fa.accounts"
	_view_name = "fa.accounts/list"
	_description = "Genaral Model Account"

class ViewModelM2MListFaAccountsTax(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.tax"
	_view_name = "fa.accounts.tax/m2mlist"
	_description = "Genaral Model Account"

class ViewModelM2MListFaAccountsTag(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.tag"
	_view_name = "fa.accounts.tag/m2mlist"
	_description = "Genaral Model Account"

class ViewModelFormModalFaAccounts(ViewModelFormModalController):
	_name = "form.modal:fa.accounts"
	_view_name = "fa.accounts/form.modal"
	_description = "Genaral Model Account"

class ViewModelFormFaAccounts(ViewModelFormController):
	_name = "form:fa.accounts"
	_view_name = "fa.accounts/form"
	_description = "Genaral Model Account"
