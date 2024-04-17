from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmInvoiceItemTexts(ViewModelFindController):
	_name = "find:crm.invoice.item.texts"
	_view_name = "crm.invoice.item.texts/find"
	_description = "CRM Invoce Item Texts"

class ViewModelO2MFormCrmInvoiceItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:crm.invoice.item.texts"
	_view_name = "crm.invoice.item.texts/o2m-form"
	_description = "CRM Invoce Item Texts"

class ViewModelO2MListCrmInvoiceItemTexts(ViewModelO2MListController):
	_name = "o2m-list:crm.invoice.item.texts"
	_view_name = "crm.invoice.item.texts/o2m-list"
	_description = "CRM Invoce Item Texts"
