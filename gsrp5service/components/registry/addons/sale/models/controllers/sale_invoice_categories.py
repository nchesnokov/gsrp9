from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchSaleInvoiceCategories(ViewModelSearchController):
	_name = "search:sale.invoice.categories"
	_view_name = "sale.invoice.categories/search"
	_description = "Category Sale Invoice"

class ViewModelFindSaleInvoiceCategories(ViewModelFindController):
	_name = "find:sale.invoice.categories"
	_view_name = "sale.invoice.categories/find"
	_description = "Category Sale Invoice"

class ViewModelListSaleInvoiceCategories(ViewModelListController):
	_name = "list:sale.invoice.categories"
	_view_name = "sale.invoice.categories/list"
	_description = "Category Sale Invoice"

class ViewModelFormModalSaleInvoiceCategories(ViewModelFormModalController):
	_name = "form.modal:sale.invoice.categories"
	_view_name = "sale.invoice.categories/form.modal"
	_description = "Category Sale Invoice"

class ViewModelFormSaleInvoiceCategories(ViewModelFormController):
	_name = "form:sale.invoice.categories"
	_view_name = "sale.invoice.categories/form"
	_description = "Category Sale Invoice"

class ViewModelTreeSaleInvoiceCategories(ViewModelTreeController):
	_name = "tree:sale.invoice.categories"
	_view_name = "sale.invoice.categories/tree"
	_description = "Category Sale Invoice"
