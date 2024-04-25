from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelM2MListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountsTax(ViewModelSearchController):
	_name = "search:fa.accounts.tax"
	_view_name = "fa.accounts.tax/search"
	_description = "General Model Accounts Tax"

class ViewModelFindFaAccountsTax(ViewModelFindController):
	_name = "find:fa.accounts.tax"
	_view_name = "fa.accounts.tax/find"
	_description = "General Model Accounts Tax"

class ViewModelListFaAccountsTax(ViewModelListController):
	_name = "list:fa.accounts.tax"
	_view_name = "fa.accounts.tax/list"
	_description = "General Model Accounts Tax"

class ViewModelM2MListFaAccountsTax(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.tax"
	_view_name = "fa.accounts.tax/m2mlist"
	_description = "General Model Accounts Tax"

class ViewModelM2MListFaAccountsTag(ViewModelM2MListController):
	_name = "m2mlist:fa.accounts.tag"
	_view_name = "fa.accounts.tag/m2mlist"
	_description = "General Model Accounts Tax"

class ViewModelFormModalFaAccountsTax(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.tax"
	_view_name = "fa.accounts.tax/form.modal"
	_description = "General Model Accounts Tax"

class ViewModelFormFaAccountsTax(ViewModelFormController):
	_name = "form:fa.accounts.tax"
	_view_name = "fa.accounts.tax/form"
	_description = "General Model Accounts Tax"
