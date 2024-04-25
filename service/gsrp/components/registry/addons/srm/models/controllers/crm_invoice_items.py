from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmInvoiceItems(ViewModelFindController):
	_name = "find:crm.invoice.items"
	_view_name = "crm.invoice.items/find"
	_description = "CRMs Invoice Items"

class ViewModelO2MFormCrmInvoiceItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.invoice.items"
	_view_name = "crm.invoice.items/o2m-form"
	_description = "CRMs Invoice Items"

class ViewModelO2MListCrmInvoiceItems(ViewModelO2MListController):
	_name = "o2m-list:crm.invoice.items"
	_view_name = "crm.invoice.items/o2m-list"
	_description = "CRMs Invoice Items"
