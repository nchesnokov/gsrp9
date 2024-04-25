from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchSaleInvoices(ViewModelSearchController):
	_name = "search:sale.invoices"
	_view_name = "sale.invoices/search"
	_description = "Sale Invoices"

class ViewModelFindSaleInvoices(ViewModelFindController):
	_name = "find:sale.invoices"
	_view_name = "sale.invoices/find"
	_description = "Sale Invoices"

class ViewModelListSaleInvoices(ViewModelListController):
	_name = "list:sale.invoices"
	_view_name = "sale.invoices/list"
	_description = "Sale Invoices"

class ViewModelFormModalSaleInvoices(ViewModelFormModalController):
	_name = "form.modal:sale.invoices"
	_view_name = "sale.invoices/form.modal"
	_description = "Sale Invoices"

class ViewModelFormSaleInvoices(ViewModelFormController):
	_name = "form:sale.invoices"
	_view_name = "sale.invoices/form"
	_description = "Sale Invoices"

class ViewModelCalendarSaleInvoices(ViewModelCalendarController):
	_name = "calendar:sale.invoices"
	_view_name = "sale.invoices/calendar"
	_description = "Sale Invoices"

class ViewModelGraphSaleInvoices(ViewModelGraphController):
	_name = "graph:sale.invoices"
	_view_name = "sale.invoices/graph"
	_description = "Sale Invoices"

class ViewModelKanbanSaleInvoices(ViewModelKanbanController):
	_name = "kanban:sale.invoices"
	_view_name = "sale.invoices/kanban"
	_description = "Sale Invoices"

class ViewModelMdxSaleInvoices(ViewModelMdxController):
	_name = "mdx:sale.invoices"
	_view_name = "sale.invoices/mdx"
	_description = "Sale Invoices"
