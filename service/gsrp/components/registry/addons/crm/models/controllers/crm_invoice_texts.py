from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmInvoiceTexts(ViewModelFindController):
	_name = "find:crm.invoice.texts"
	_view_name = "crm.invoice.texts/find"
	_description = "CRM Invoce Texts"

class ViewModelO2MFormCrmInvoiceTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.invoice.texts"
	_view_name = "crm.invoice.texts/o2m-form"
	_description = "CRM Invoce Texts"

class ViewModelO2MListCrmInvoiceTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.invoice.texts"
	_view_name = "crm.invoice.texts/o2m-list"
	_description = "CRM Invoce Texts"
