from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoicePricing(ViewModelFindController):
	_name = "find:purchase.invoice.pricing"
	_view_name = "purchase.invoice.pricing/find"
	_description = "Purchase Invoice Pricing"

class ViewModelO2MFormPurchaseInvoicePricing(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.pricing"
	_view_name = "purchase.invoice.pricing/o2m-form"
	_description = "Purchase Invoice Pricing"

class ViewModelO2MListPurchaseInvoicePricing(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.pricing"
	_view_name = "purchase.invoice.pricing/o2m-list"
	_description = "Purchase Invoice Pricing"
