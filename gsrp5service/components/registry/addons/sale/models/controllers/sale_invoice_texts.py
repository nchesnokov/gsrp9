from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleInvoiceTexts(ViewModelFindController):
	_name = "find:sale.invoice.texts"
	_view_name = "sale.invoice.texts/find"
	_description = "Sale Invoce Texts"

class ViewModelO2MFormSaleInvoiceTexts(ViewModelO2MFormController):
	_name = "o2m-form:sale.invoice.texts"
	_view_name = "sale.invoice.texts/o2m-form"
	_description = "Sale Invoce Texts"

class ViewModelO2MListSaleInvoiceTexts(ViewModelO2MListController):
	_name = "o2m-list:sale.invoice.texts"
	_view_name = "sale.invoice.texts/o2m-list"
	_description = "Sale Invoce Texts"
