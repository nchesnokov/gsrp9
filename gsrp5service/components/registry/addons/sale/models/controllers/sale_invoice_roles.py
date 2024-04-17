from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleInvoiceRoles(ViewModelFindController):
	_name = "find:sale.invoice.roles"
	_view_name = "sale.invoice.roles/find"
	_description = "sale Invoice Roles"

class ViewModelO2MFormSaleInvoiceRoles(ViewModelO2MFormController):
	_name = "o2m-form:sale.invoice.roles"
	_view_name = "sale.invoice.roles/o2m-form"
	_description = "sale Invoice Roles"

class ViewModelO2MListSaleInvoiceRoles(ViewModelO2MListController):
	_name = "o2m-list:sale.invoice.roles"
	_view_name = "sale.invoice.roles/o2m-list"
	_description = "sale Invoice Roles"
