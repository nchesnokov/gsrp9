from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjPricingGroupLevels(ViewModelSearchController):
	_name = "search:prj.pricing.group.levels"
	_view_name = "prj.pricing.group.levels/search"
	_description = "Project Pricing Group Levels"

class ViewModelFindPrjPricingGroupLevels(ViewModelFindController):
	_name = "find:prj.pricing.group.levels"
	_view_name = "prj.pricing.group.levels/find"
	_description = "Project Pricing Group Levels"

class ViewModelListPrjPricingGroupLevels(ViewModelListController):
	_name = "list:prj.pricing.group.levels"
	_view_name = "prj.pricing.group.levels/list"
	_description = "Project Pricing Group Levels"

class ViewModelFormModalPrjPricingGroupLevels(ViewModelFormModalController):
	_name = "form.modal:prj.pricing.group.levels"
	_view_name = "prj.pricing.group.levels/form.modal"
	_description = "Project Pricing Group Levels"

class ViewModelFormPrjPricingGroupLevels(ViewModelFormController):
	_name = "form:prj.pricing.group.levels"
	_view_name = "prj.pricing.group.levels/form"
	_description = "Project Pricing Group Levels"
