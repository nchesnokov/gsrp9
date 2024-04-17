from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchCrmPricingGroupLevels(ViewModelSearchController):
	_name = "search:crm.pricing.group.levels"
	_view_name = "crm.pricing.group.levels/search"
	_description = "CRM Pricing Group Levels"

class ViewModelFindCrmPricingGroupLevels(ViewModelFindController):
	_name = "find:crm.pricing.group.levels"
	_view_name = "crm.pricing.group.levels/find"
	_description = "CRM Pricing Group Levels"

class ViewModelListCrmPricingGroupLevels(ViewModelListController):
	_name = "list:crm.pricing.group.levels"
	_view_name = "crm.pricing.group.levels/list"
	_description = "CRM Pricing Group Levels"

class ViewModelFormModalCrmPricingGroupLevels(ViewModelFormModalController):
	_name = "form.modal:crm.pricing.group.levels"
	_view_name = "crm.pricing.group.levels/form.modal"
	_description = "CRM Pricing Group Levels"

class ViewModelFormCrmPricingGroupLevels(ViewModelFormController):
	_name = "form:crm.pricing.group.levels"
	_view_name = "crm.pricing.group.levels/form"
	_description = "CRM Pricing Group Levels"
