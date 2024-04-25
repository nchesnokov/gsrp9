from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPurchasePricingGroupLevels(ViewModelSearchController):
	_name = "search:purchase.pricing.group.levels"
	_view_name = "purchase.pricing.group.levels/search"
	_description = "Purchase Pricing Group Levels"

class ViewModelFindPurchasePricingGroupLevels(ViewModelFindController):
	_name = "find:purchase.pricing.group.levels"
	_view_name = "purchase.pricing.group.levels/find"
	_description = "Purchase Pricing Group Levels"

class ViewModelListPurchasePricingGroupLevels(ViewModelListController):
	_name = "list:purchase.pricing.group.levels"
	_view_name = "purchase.pricing.group.levels/list"
	_description = "Purchase Pricing Group Levels"

class ViewModelFormModalPurchasePricingGroupLevels(ViewModelFormModalController):
	_name = "form.modal:purchase.pricing.group.levels"
	_view_name = "purchase.pricing.group.levels/form.modal"
	_description = "Purchase Pricing Group Levels"

class ViewModelFormPurchasePricingGroupLevels(ViewModelFormController):
	_name = "form:purchase.pricing.group.levels"
	_view_name = "purchase.pricing.group.levels/form"
	_description = "Purchase Pricing Group Levels"
