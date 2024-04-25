from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchFaReconcileModelTemplate(ViewModelSearchController):
	_name = "search:fa.reconcile.model.template"
	_view_name = "fa.reconcile.model.template/search"
	_description = "Reconcile Model Template"

class ViewModelFindFaReconcileModelTemplate(ViewModelFindController):
	_name = "find:fa.reconcile.model.template"
	_view_name = "fa.reconcile.model.template/find"
	_description = "Reconcile Model Template"

class ViewModelListFaReconcileModelTemplate(ViewModelListController):
	_name = "list:fa.reconcile.model.template"
	_view_name = "fa.reconcile.model.template/list"
	_description = "Reconcile Model Template"

class ViewModelFormModalFaReconcileModelTemplate(ViewModelFormModalController):
	_name = "form.modal:fa.reconcile.model.template"
	_view_name = "fa.reconcile.model.template/form.modal"
	_description = "Reconcile Model Template"

class ViewModelFormFaReconcileModelTemplate(ViewModelFormController):
	_name = "form:fa.reconcile.model.template"
	_view_name = "fa.reconcile.model.template/form"
	_description = "Reconcile Model Template"
