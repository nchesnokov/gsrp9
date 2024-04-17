from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchPurchaseInvoices(ViewModelSearchController):
	_name = "search:purchase.invoices"
	_view_name = "purchase.invoices/search"
	_description = "Purchase Invoice"

class ViewModelFindPurchaseInvoices(ViewModelFindController):
	_name = "find:purchase.invoices"
	_view_name = "purchase.invoices/find"
	_description = "Purchase Invoice"

class ViewModelListPurchaseInvoices(ViewModelListController):
	_name = "list:purchase.invoices"
	_view_name = "purchase.invoices/list"
	_description = "Purchase Invoice"

class ViewModelFormModalPurchaseInvoices(ViewModelFormModalController):
	_name = "form.modal:purchase.invoices"
	_view_name = "purchase.invoices/form.modal"
	_description = "Purchase Invoice"

class ViewModelFormPurchaseInvoices(ViewModelFormController):
	_name = "form:purchase.invoices"
	_view_name = "purchase.invoices/form"
	_description = "Purchase Invoice"

class ViewModelCalendarPurchaseInvoices(ViewModelCalendarController):
	_name = "calendar:purchase.invoices"
	_view_name = "purchase.invoices/calendar"
	_description = "Purchase Invoice"

class ViewModelGraphPurchaseInvoices(ViewModelGraphController):
	_name = "graph:purchase.invoices"
	_view_name = "purchase.invoices/graph"
	_description = "Purchase Invoice"

class ViewModelKanbanPurchaseInvoices(ViewModelKanbanController):
	_name = "kanban:purchase.invoices"
	_view_name = "purchase.invoices/kanban"
	_description = "Purchase Invoice"

class ViewModelMdxPurchaseInvoices(ViewModelMdxController):
	_name = "mdx:purchase.invoices"
	_view_name = "purchase.invoices/mdx"
	_description = "Purchase Invoice"
