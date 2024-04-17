from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindMmTechnologicOrderPricing(ViewModelFindController):
	_name = "find:mm.technologic.order.pricing"
	_view_name = "mm.technologic.order.pricing/find"
	_description = "Technologic Order Pricing"

class ViewModelO2MFormMmTechnologicOrderPricing(ViewModelO2MFormController):
	_name = "o2m-form:mm.technologic.order.pricing"
	_view_name = "mm.technologic.order.pricing/o2m-form"
	_description = "Technologic Order Pricing"

class ViewModelO2MListMmTechnologicOrderPricing(ViewModelO2MListController):
	_name = "o2m-list:mm.technologic.order.pricing"
	_view_name = "mm.technologic.order.pricing/o2m-list"
	_description = "Technologic Order Pricing"
