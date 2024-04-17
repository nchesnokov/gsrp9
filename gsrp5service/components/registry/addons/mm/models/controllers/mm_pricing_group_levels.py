from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmPricingGroupLevels(ViewModelSearchController):
	_name = "search:mm.pricing.group.levels"
	_view_name = "mm.pricing.group.levels/search"
	_description = "Production Pricing Group Levels"

class ViewModelFindMmPricingGroupLevels(ViewModelFindController):
	_name = "find:mm.pricing.group.levels"
	_view_name = "mm.pricing.group.levels/find"
	_description = "Production Pricing Group Levels"

class ViewModelListMmPricingGroupLevels(ViewModelListController):
	_name = "list:mm.pricing.group.levels"
	_view_name = "mm.pricing.group.levels/list"
	_description = "Production Pricing Group Levels"

class ViewModelFormModalMmPricingGroupLevels(ViewModelFormModalController):
	_name = "form.modal:mm.pricing.group.levels"
	_view_name = "mm.pricing.group.levels/form.modal"
	_description = "Production Pricing Group Levels"

class ViewModelFormMmPricingGroupLevels(ViewModelFormController):
	_name = "form:mm.pricing.group.levels"
	_view_name = "mm.pricing.group.levels/form"
	_description = "Production Pricing Group Levels"
