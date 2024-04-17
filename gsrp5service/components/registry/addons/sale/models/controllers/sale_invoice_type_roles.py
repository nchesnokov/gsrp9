from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleInvoiceTypeRoles(ViewModelFindController):
	_name = "find:sale.invoice.type.roles"
	_view_name = "sale.invoice.type.roles/find"
	_description = "Role sale Invoice Types"

class ViewModelO2MFormSaleInvoiceTypeRoles(ViewModelO2MFormController):
	_name = "o2m-form:sale.invoice.type.roles"
	_view_name = "sale.invoice.type.roles/o2m-form"
	_description = "Role sale Invoice Types"

class ViewModelO2MListSaleInvoiceTypeRoles(ViewModelO2MListController):
	_name = "o2m-list:sale.invoice.type.roles"
	_view_name = "sale.invoice.type.roles/o2m-list"
	_description = "Role sale Invoice Types"
