from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleInvoiceItemTexts(ViewModelFindController):
	_name = "find:sale.invoice.item.texts"
	_view_name = "sale.invoice.item.texts/find"
	_description = "Sale Invoce Item Texts"

class ViewModelO2MFormSaleInvoiceItemTexts(ViewModelO2MFormController):
	_name = "o2m-form:sale.invoice.item.texts"
	_view_name = "sale.invoice.item.texts/o2m-form"
	_description = "Sale Invoce Item Texts"

class ViewModelO2MListSaleInvoiceItemTexts(ViewModelO2MListController):
	_name = "o2m-list:sale.invoice.item.texts"
	_view_name = "sale.invoice.item.texts/o2m-list"
	_description = "Sale Invoce Item Texts"
