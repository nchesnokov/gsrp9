from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmResponsePricing(ViewModelFindController):
	_name = "find:srm.response.pricing"
	_view_name = "srm.response.pricing/find"
	_description = "SRM Response Pricing"

class ViewModelO2MFormSrmResponsePricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.response.pricing"
	_view_name = "srm.response.pricing/o2m-form"
	_description = "SRM Response Pricing"

class ViewModelO2MListSrmResponsePricing(ViewModelO2MListController):
	_name = "o2m-list:srm.response.pricing"
	_view_name = "srm.response.pricing/o2m-list"
	_description = "SRM Response Pricing"
