from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSaleInvoiceTypes(ViewModelSearchController):
	_name = "search:sale.invoice.types"
	_view_name = "sale.invoice.types/search"
	_description = "Types Sale Invoice"

class ViewModelFindSaleInvoiceTypes(ViewModelFindController):
	_name = "find:sale.invoice.types"
	_view_name = "sale.invoice.types/find"
	_description = "Types Sale Invoice"

class ViewModelListSaleInvoiceTypes(ViewModelListController):
	_name = "list:sale.invoice.types"
	_view_name = "sale.invoice.types/list"
	_description = "Types Sale Invoice"

class ViewModelFormModalSaleInvoiceTypes(ViewModelFormModalController):
	_name = "form.modal:sale.invoice.types"
	_view_name = "sale.invoice.types/form.modal"
	_description = "Types Sale Invoice"

class ViewModelFormSaleInvoiceTypes(ViewModelFormController):
	_name = "form:sale.invoice.types"
	_view_name = "sale.invoice.types/form"
	_description = "Types Sale Invoice"
