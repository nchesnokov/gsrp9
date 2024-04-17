from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleInvoiceItemRoles(ViewModelFindController):
	_name = "find:sale.invoice.item.roles"
	_view_name = "sale.invoice.item.roles/find"
	_description = "Sale Invoice Item Roles"

class ViewModelO2MFormSaleInvoiceItemRoles(ViewModelO2MFormController):
	_name = "o2m-form:sale.invoice.item.roles"
	_view_name = "sale.invoice.item.roles/o2m-form"
	_description = "Sale Invoice Item Roles"

class ViewModelO2MListSaleInvoiceItemRoles(ViewModelO2MListController):
	_name = "o2m-list:sale.invoice.item.roles"
	_view_name = "sale.invoice.item.roles/o2m-list"
	_description = "Sale Invoice Item Roles"
