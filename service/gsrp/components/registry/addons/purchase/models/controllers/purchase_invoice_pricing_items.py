from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseInvoicePricingItems(ViewModelFindController):
	_name = "find:purchase.invoice.pricing.items"
	_view_name = "purchase.invoice.pricing.items/find"
	_description = "Purchase Invoice Item Pricing"

class ViewModelO2MFormPurchaseInvoicePricingItems(ViewModelO2MFormController):
	_name = "o2m-form:purchase.invoice.pricing.items"
	_view_name = "purchase.invoice.pricing.items/o2m-form"
	_description = "Purchase Invoice Item Pricing"

class ViewModelO2MListPurchaseInvoicePricingItems(ViewModelO2MListController):
	_name = "o2m-list:purchase.invoice.pricing.items"
	_view_name = "purchase.invoice.pricing.items/o2m-list"
	_description = "Purchase Invoice Item Pricing"
