from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmInvoiceCategories(ViewModelSearchController):
	_name = "search:crm.invoice.categories"
	_view_name = "crm.invoice.categories/search"
	_description = "Category CRM Invoice"

class ViewModelFindCrmInvoiceCategories(ViewModelFindController):
	_name = "find:crm.invoice.categories"
	_view_name = "crm.invoice.categories/find"
	_description = "Category CRM Invoice"

class ViewModelListCrmInvoiceCategories(ViewModelListController):
	_name = "list:crm.invoice.categories"
	_view_name = "crm.invoice.categories/list"
	_description = "Category CRM Invoice"

class ViewModelFormModalCrmInvoiceCategories(ViewModelFormModalController):
	_name = "form.modal:crm.invoice.categories"
	_view_name = "crm.invoice.categories/form.modal"
	_description = "Category CRM Invoice"

class ViewModelFormCrmInvoiceCategories(ViewModelFormController):
	_name = "form:crm.invoice.categories"
	_view_name = "crm.invoice.categories/form"
	_description = "Category CRM Invoice"

class ViewModelTreeCrmInvoiceCategories(ViewModelTreeController):
	_name = "tree:crm.invoice.categories"
	_view_name = "crm.invoice.categories/tree"
	_description = "Category CRM Invoice"
