from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionPricing(ViewModelFindController):
	_name = "find:srm.evolution.pricing"
	_view_name = "srm.evolution.pricing/find"
	_description = "SRM Evolution Pricing"

class ViewModelO2MFormSrmEvolutionPricing(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.pricing"
	_view_name = "srm.evolution.pricing/o2m-form"
	_description = "SRM Evolution Pricing"

class ViewModelO2MListSrmEvolutionPricing(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.pricing"
	_view_name = "srm.evolution.pricing/o2m-list"
	_description = "SRM Evolution Pricing"
