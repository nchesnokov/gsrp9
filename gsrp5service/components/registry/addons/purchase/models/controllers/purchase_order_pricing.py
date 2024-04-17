from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderPricing(ViewModelFindController):
	_name = "find:purchase.order.pricing"
	_view_name = "purchase.order.pricing/find"
	_description = "Purchase Order Pricing"

class ViewModelO2MFormPurchaseOrderPricing(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.pricing"
	_view_name = "purchase.order.pricing/o2m-form"
	_description = "Purchase Order Pricing"

class ViewModelO2MListPurchaseOrderPricing(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.pricing"
	_view_name = "purchase.order.pricing/o2m-list"
	_description = "Purchase Order Pricing"
