from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderPricing(ViewModelFindController):
	_name = "find:crm.order.pricing"
	_view_name = "crm.order.pricing/find"
	_description = "CRM Order Pricing"

class ViewModelO2MFormCrmOrderPricing(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.pricing"
	_view_name = "crm.order.pricing/o2m-form"
	_description = "CRM Order Pricing"

class ViewModelO2MListCrmOrderPricing(ViewModelO2MListController):
	_name = "o2m-list:crm.order.pricing"
	_view_name = "crm.order.pricing/o2m-list"
	_description = "CRM Order Pricing"
