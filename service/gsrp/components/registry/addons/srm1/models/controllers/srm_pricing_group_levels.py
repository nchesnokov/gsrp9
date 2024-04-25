from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmPricingGroupLevels(ViewModelSearchController):
	_name = "search:srm.pricing.group.levels"
	_view_name = "srm.pricing.group.levels/search"
	_description = "SRM Pricing Group Levels"

class ViewModelFindSrmPricingGroupLevels(ViewModelFindController):
	_name = "find:srm.pricing.group.levels"
	_view_name = "srm.pricing.group.levels/find"
	_description = "SRM Pricing Group Levels"

class ViewModelListSrmPricingGroupLevels(ViewModelListController):
	_name = "list:srm.pricing.group.levels"
	_view_name = "srm.pricing.group.levels/list"
	_description = "SRM Pricing Group Levels"

class ViewModelFormModalSrmPricingGroupLevels(ViewModelFormModalController):
	_name = "form.modal:srm.pricing.group.levels"
	_view_name = "srm.pricing.group.levels/form.modal"
	_description = "SRM Pricing Group Levels"

class ViewModelFormSrmPricingGroupLevels(ViewModelFormController):
	_name = "form:srm.pricing.group.levels"
	_view_name = "srm.pricing.group.levels/form"
	_description = "SRM Pricing Group Levels"
