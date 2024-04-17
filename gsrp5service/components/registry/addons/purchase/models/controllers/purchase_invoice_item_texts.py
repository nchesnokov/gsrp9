from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoiceItemTexts(ViewModelFindController):
	_name = "find:purchase.invoice.item.texts"
	_view_name = "purchase.invoice.item.texts/find"
	_description = "Purchase Invoce Item Texts"

class ViewModelO2MFormPurchaseInvoiceItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.item.texts"
	_view_name = "purchase.invoice.item.texts/o2m-form"
	_description = "Purchase Invoce Item Texts"

class ViewModelO2MListPurchaseInvoiceItemTexts(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.item.texts"
	_view_name = "purchase.invoice.item.texts/o2m-list"
	_description = "Purchase Invoce Item Texts"
