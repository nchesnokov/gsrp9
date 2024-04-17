from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleInvoiceItems(ViewModelFindController):
	_name = "find:sale.invoice.items"
	_view_name = "sale.invoice.items/find"
	_description = "Sales Invoice Items"

class ViewModelO2MFormSaleInvoiceItems(ViewModelO2MFormController):
	_name = "o2m-form:sale.invoice.items"
	_view_name = "sale.invoice.items/o2m-form"
	_description = "Sales Invoice Items"

class ViewModelO2MListSaleInvoiceItems(ViewModelO2MListController):
	_name = "o2m-list:sale.invoice.items"
	_view_name = "sale.invoice.items/o2m-list"
	_description = "Sales Invoice Items"
