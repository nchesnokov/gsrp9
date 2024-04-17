from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindPurchaseOrderPricingItems(ViewModelFindController):
	_name = "find:purchase.order.pricing.items"
	_view_name = "purchase.order.pricing.items/find"
	_description = "Purchase Order Item Pricing"

class ViewModelO2MFormPurchaseOrderPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:purchase.order.pricing.items"
	_view_name = "purchase.order.pricing.items/o2m-form"
	_description = "Purchase Order Item Pricing"

class ViewModelO2MListPurchaseOrderPricingItems(ViewModelO2MListController):
	_name = "o2m-list:purchase.order.pricing.items"
	_view_name = "purchase.order.pricing.items/o2m-list"
	_description = "Purchase Order Item Pricing"
