from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoiceTexts(ViewModelFindController):
	_name = "find:purchase.invoice.texts"
	_view_name = "purchase.invoice.texts/find"
	_description = "Purchase Invoce Texts"

class ViewModelO2MFormPurchaseInvoiceTexts(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.texts"
	_view_name = "purchase.invoice.texts/o2m-form"
	_description = "Purchase Invoce Texts"

class ViewModelO2MListPurchaseInvoiceTexts(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.texts"
	_view_name = "purchase.invoice.texts/o2m-list"
	_description = "Purchase Invoce Texts"
