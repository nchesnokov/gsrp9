from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmRegionCategories(ViewModelSearchController):
	_name = "search:crm.region.categories"
	_view_name = "crm.region.categories/search"
	_description = "Categories CRM Region"

class ViewModelFindCrmRegionCategories(ViewModelFindController):
	_name = "find:crm.region.categories"
	_view_name = "crm.region.categories/find"
	_description = "Categories CRM Region"

class ViewModelListCrmRegionCategories(ViewModelListController):
	_name = "list:crm.region.categories"
	_view_name = "crm.region.categories/list"
	_description = "Categories CRM Region"

class ViewModelFormModalCrmRegionCategories(ViewModelFormModalController):
	_name = "form.modal:crm.region.categories"
	_view_name = "crm.region.categories/form.modal"
	_description = "Categories CRM Region"

class ViewModelFormCrmRegionCategories(ViewModelFormController):
	_name = "form:crm.region.categories"
	_view_name = "crm.region.categories/form"
	_description = "Categories CRM Region"

class ViewModelTreeCrmRegionCategories(ViewModelTreeController):
	_name = "tree:crm.region.categories"
	_view_name = "crm.region.categories/tree"
	_description = "Categories CRM Region"
