from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindCrmRequestPricing(ViewModelFindController):
	_name = "find:crm.request.pricing"
	_view_name = "crm.request.pricing/find"
	_description = "CRM Request Pricing"

class ViewModelO2MFormCrmRequestPricing(ViewModelO2MFormController):
	_name = "o2m-form:crm.request.pricing"
	_view_name = "crm.request.pricing/o2m-form"
	_description = "CRM Request Pricing"

class ViewModelO2MListCrmRequestPricing(ViewModelO2MListController):
	_name = "o2m-list:crm.request.pricing"
	_view_name = "crm.request.pricing/o2m-list"
	_description = "CRM Request Pricing"
