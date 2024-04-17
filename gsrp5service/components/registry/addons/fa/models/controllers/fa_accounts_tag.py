from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountsTag(ViewModelSearchController):
	_name = "search:fa.accounts.tag"
	_view_name = "fa.accounts.tag/search"
	_description = "General Model Account Tag"

class ViewModelFindFaAccountsTag(ViewModelFindController):
	_name = "find:fa.accounts.tag"
	_view_name = "fa.accounts.tag/find"
	_description = "General Model Account Tag"

class ViewModelListFaAccountsTag(ViewModelListController):
	_name = "list:fa.accounts.tag"
	_view_name = "fa.accounts.tag/list"
	_description = "General Model Account Tag"

class ViewModelFormModalFaAccountsTag(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.tag"
	_view_name = "fa.accounts.tag/form.modal"
	_description = "General Model Account Tag"

class ViewModelFormFaAccountsTag(ViewModelFormController):
	_name = "form:fa.accounts.tag"
	_view_name = "fa.accounts.tag/form"
	_description = "General Model Account Tag"
