from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaAccountsReconcileModel(ViewModelSearchController):
	_name = "search:fa.accounts.reconcile.model"
	_view_name = "fa.accounts.reconcile.model/search"
	_description = "General Model Accounts Reconcile"

class ViewModelFindFaAccountsReconcileModel(ViewModelFindController):
	_name = "find:fa.accounts.reconcile.model"
	_view_name = "fa.accounts.reconcile.model/find"
	_description = "General Model Accounts Reconcile"

class ViewModelListFaAccountsReconcileModel(ViewModelListController):
	_name = "list:fa.accounts.reconcile.model"
	_view_name = "fa.accounts.reconcile.model/list"
	_description = "General Model Accounts Reconcile"

class ViewModelFormModalFaAccountsReconcileModel(ViewModelFormModalController):
	_name = "form.modal:fa.accounts.reconcile.model"
	_view_name = "fa.accounts.reconcile.model/form.modal"
	_description = "General Model Accounts Reconcile"

class ViewModelFormFaAccountsReconcileModel(ViewModelFormController):
	_name = "form:fa.accounts.reconcile.model"
	_view_name = "fa.accounts.reconcile.model/form"
	_description = "General Model Accounts Reconcile"
