from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSalePricingGroupLevels(ViewModelSearchController):
	_name = "search:sale.pricing.group.levels"
	_view_name = "sale.pricing.group.levels/search"
	_description = "Sale Pricing Group Levels"

class ViewModelFindSalePricingGroupLevels(ViewModelFindController):
	_name = "find:sale.pricing.group.levels"
	_view_name = "sale.pricing.group.levels/find"
	_description = "Sale Pricing Group Levels"

class ViewModelListSalePricingGroupLevels(ViewModelListController):
	_name = "list:sale.pricing.group.levels"
	_view_name = "sale.pricing.group.levels/list"
	_description = "Sale Pricing Group Levels"

class ViewModelFormModalSalePricingGroupLevels(ViewModelFormModalController):
	_name = "form.modal:sale.pricing.group.levels"
	_view_name = "sale.pricing.group.levels/form.modal"
	_description = "Sale Pricing Group Levels"

class ViewModelFormSalePricingGroupLevels(ViewModelFormController):
	_name = "form:sale.pricing.group.levels"
	_view_name = "sale.pricing.group.levels/form"
	_description = "Sale Pricing Group Levels"
