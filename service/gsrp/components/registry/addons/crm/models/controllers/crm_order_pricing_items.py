from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmOrderPricingItems(ViewModelFindController):
	_name = "find:crm.order.pricing.items"
	_view_name = "crm.order.pricing.items/find"
	_description = "CRM Order Item Pricing"

class ViewModelO2MFormCrmOrderPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.order.pricing.items"
	_view_name = "crm.order.pricing.items/o2m-form"
	_description = "CRM Order Item Pricing"

class ViewModelO2MListCrmOrderPricingItems(ViewModelO2MListController):
	_name = "o2m-list:crm.order.pricing.items"
	_view_name = "crm.order.pricing.items/o2m-list"
	_description = "CRM Order Item Pricing"
