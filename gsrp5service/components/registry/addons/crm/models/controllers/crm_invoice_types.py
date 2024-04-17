from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmInvoiceTypes(ViewModelSearchController):
	_name = "search:crm.invoice.types"
	_view_name = "crm.invoice.types/search"
	_description = "Types CRM Invoice"

class ViewModelFindCrmInvoiceTypes(ViewModelFindController):
	_name = "find:crm.invoice.types"
	_view_name = "crm.invoice.types/find"
	_description = "Types CRM Invoice"

class ViewModelListCrmInvoiceTypes(ViewModelListController):
	_name = "list:crm.invoice.types"
	_view_name = "crm.invoice.types/list"
	_description = "Types CRM Invoice"

class ViewModelFormModalCrmInvoiceTypes(ViewModelFormModalController):
	_name = "form.modal:crm.invoice.types"
	_view_name = "crm.invoice.types/form.modal"
	_description = "Types CRM Invoice"

class ViewModelFormCrmInvoiceTypes(ViewModelFormController):
	_name = "form:crm.invoice.types"
	_view_name = "crm.invoice.types/form"
	_description = "Types CRM Invoice"
