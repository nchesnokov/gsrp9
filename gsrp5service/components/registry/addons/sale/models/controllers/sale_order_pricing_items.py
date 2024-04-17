from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderPricingItems(ViewModelFindController):
	_name = "find:sale.order.pricing.items"
	_view_name = "sale.order.pricing.items/find"
	_description = "Sale Order Item Pricing"

class ViewModelO2MFormSaleOrderPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.pricing.items"
	_view_name = "sale.order.pricing.items/o2m-form"
	_description = "Sale Order Item Pricing"

class ViewModelO2MListSaleOrderPricingItems(ViewModelO2MListController):
	_name = "o2m-list:sale.order.pricing.items"
	_view_name = "sale.order.pricing.items/o2m-list"
	_description = "Sale Order Item Pricing"
