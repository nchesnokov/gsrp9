from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelCalendarController
from gsrp5service.obj.controller.controller import ViewModelGraphController
from gsrp5service.obj.controller.controller import ViewModelKanbanController
from gsrp5service.obj.controller.controller import ViewModelMdxController

class ViewModelSearchCrmInvoices(ViewModelSearchController):
	_name = "search:crm.invoices"
	_view_name = "crm.invoices/search"
	_description = "CRM Invoices"

class ViewModelFindCrmInvoices(ViewModelFindController):
	_name = "find:crm.invoices"
	_view_name = "crm.invoices/find"
	_description = "CRM Invoices"

class ViewModelListCrmInvoices(ViewModelListController):
	_name = "list:crm.invoices"
	_view_name = "crm.invoices/list"
	_description = "CRM Invoices"

class ViewModelFormModalCrmInvoices(ViewModelFormModalController):
	_name = "form.modal:crm.invoices"
	_view_name = "crm.invoices/form.modal"
	_description = "CRM Invoices"

class ViewModelFormCrmInvoices(ViewModelFormController):
	_name = "form:crm.invoices"
	_view_name = "crm.invoices/form"
	_description = "CRM Invoices"

class ViewModelCalendarCrmInvoices(ViewModelCalendarController):
	_name = "calendar:crm.invoices"
	_view_name = "crm.invoices/calendar"
	_description = "CRM Invoices"

class ViewModelGraphCrmInvoices(ViewModelGraphController):
	_name = "graph:crm.invoices"
	_view_name = "crm.invoices/graph"
	_description = "CRM Invoices"

class ViewModelKanbanCrmInvoices(ViewModelKanbanController):
	_name = "kanban:crm.invoices"
	_view_name = "crm.invoices/kanban"
	_description = "CRM Invoices"

class ViewModelMdxCrmInvoices(ViewModelMdxController):
	_name = "mdx:crm.invoices"
	_view_name = "crm.invoices/mdx"
	_description = "CRM Invoices"
