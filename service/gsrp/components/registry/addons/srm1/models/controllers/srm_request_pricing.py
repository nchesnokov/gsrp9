from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmRequestPricing(ViewModelFindController):
	_name = "find:srm.request.pricing"
	_view_name = "srm.request.pricing/find"
	_description = "SRM Request Pricing"

class ViewModelO2MFormSrmRequestPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.request.pricing"
	_view_name = "srm.request.pricing/o2m-form"
	_description = "SRM Request Pricing"

class ViewModelO2MListSrmRequestPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.request.pricing"
	_view_name = "srm.request.pricing/o2m-list"
	_description = "SRM Request Pricing"
