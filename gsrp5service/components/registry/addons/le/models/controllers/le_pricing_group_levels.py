from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchLePricingGroupLevels(ViewModelSearchController):
	_name = "search:le.pricing.group.levels"
	_view_name = "le.pricing.group.levels/search"
	_description = "Sale Pricing Group Levels"

class ViewModelFindLePricingGroupLevels(ViewModelFindController):
	_name = "find:le.pricing.group.levels"
	_view_name = "le.pricing.group.levels/find"
	_description = "Sale Pricing Group Levels"

class ViewModelListLePricingGroupLevels(ViewModelListController):
	_name = "list:le.pricing.group.levels"
	_view_name = "le.pricing.group.levels/list"
	_description = "Sale Pricing Group Levels"

class ViewModelFormModalLePricingGroupLevels(ViewModelFormModalController):
	_name = "form.modal:le.pricing.group.levels"
	_view_name = "le.pricing.group.levels/form.modal"
	_description = "Sale Pricing Group Levels"

class ViewModelFormLePricingGroupLevels(ViewModelFormController):
	_name = "form:le.pricing.group.levels"
	_view_name = "le.pricing.group.levels/form"
	_description = "Sale Pricing Group Levels"
