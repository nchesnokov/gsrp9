from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmProductionOrderPricing(ViewModelFindController):
	_name = "find:mm.production.order.pricing"
	_view_name = "mm.production.order.pricing/find"
	_description = "Production Order Pricing"

class ViewModelO2MFormMmProductionOrderPricing(ViewModelO2MFormController):
	_name = "o2m-form:mm.production.order.pricing"
	_view_name = "mm.production.order.pricing/o2m-form"
	_description = "Production Order Pricing"

class ViewModelO2MListMmProductionOrderPricing(ViewModelO2MListController):
	_name = "o2m-list:mm.production.order.pricing"
	_view_name = "mm.production.order.pricing/o2m-list"
	_description = "Production Order Pricing"
