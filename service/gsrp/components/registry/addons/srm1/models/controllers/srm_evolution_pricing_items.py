from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelO2MFormController
from gsrp5service.obj.controller.controller import ViewModelO2MListController

class ViewModelFindSrmEvolutionPricingItems(ViewModelFindController):
	_name = "find:srm.evolution.pricing.items"
	_view_name = "srm.evolution.pricing.items/find"
	_description = "Evolution Item Pricing"

class ViewModelO2MFormSrmEvolutionPricingItems(ViewModelO2MFormController):
	_name = "o2m-form:srm.evolution.pricing.items"
	_view_name = "srm.evolution.pricing.items/o2m-form"
	_description = "Evolution Item Pricing"

class ViewModelO2MListSrmEvolutionPricingItems(ViewModelO2MListController):
	_name = "o2m-list:srm.evolution.pricing.items"
	_view_name = "srm.evolution.pricing.items/o2m-list"
	_description = "Evolution Item Pricing"
