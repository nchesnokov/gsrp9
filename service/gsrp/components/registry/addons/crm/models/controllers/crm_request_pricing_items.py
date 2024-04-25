from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestPricingItems(ViewModelFindController):
	_name = "find:crm.request.pricing.items"
	_view_name = "crm.request.pricing.items/find"
	_description = "CRM Request Item Pricing"

class ViewModelO2MFormCrmRequestPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.pricing.items"
	_view_name = "crm.request.pricing.items/o2m-form"
	_description = "CRM Request Item Pricing"

class ViewModelO2MListCrmRequestPricingItems(ViewModelO2MListController):
	_name = "o2m-list:crm.request.pricing.items"
	_view_name = "crm.request.pricing.items/o2m-list"
	_description = "CRM Request Item Pricing"
