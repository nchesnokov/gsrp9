from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSaleOrderPricing(ViewModelFindController):
	_name = "find:sale.order.pricing"
	_view_name = "sale.order.pricing/find"
	_description = "Sale Order Pricing"

class ViewModelO2MFormSaleOrderPricing(ViewModelO2MFormController):
	_name = "o2m-form:sale.order.pricing"
	_view_name = "sale.order.pricing/o2m-form"
	_description = "Sale Order Pricing"

class ViewModelO2MListSaleOrderPricing(ViewModelO2MListController):
	_name = "o2m-list:sale.order.pricing"
	_view_name = "sale.order.pricing/o2m-list"
	_description = "Sale Order Pricing"
