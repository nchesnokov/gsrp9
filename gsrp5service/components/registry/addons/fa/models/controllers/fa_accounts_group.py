from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchFaAccountsGroup(ViewModelSearchController):
	_name = "search:fa.accounts.group"
	_view_name = "fa.accounts.group/search"
	_description = "Genaral Model Accounts Group"

class ViewModelFindFaAccountsGroup(ViewModelFindController):
	_name = "find:fa.accounts.group"
	_view_name = "fa.accounts.group/find"
	_description = "Genaral Model Accounts Group"

class ViewModelListFaAccountsGroup(ViewModelListController):
	_name = "list:fa.accounts.group"
	_view_name = "fa.accounts.group/list"
	_description = "Genaral Model Accounts Group"

class ViewModelFormModalFaAccountsGroup(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.group"
	_view_name = "fa.accounts.group/form.modal"
	_description = "Genaral Model Accounts Group"

class ViewModelFormFaAccountsGroup(ViewModelFormController):
	_name = "form:fa.accounts.group"
	_view_name = "fa.accounts.group/form"
	_description = "Genaral Model Accounts Group"

class ViewModelTreeFaAccountsGroup(ViewModelTreeController):
	_name = "tree:fa.accounts.group"
	_view_name = "fa.accounts.group/tree"
	_description = "Genaral Model Accounts Group"
