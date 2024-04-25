from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmAreaCategories(ViewModelSearchController):
	_name = "search:crm.area.categories"
	_view_name = "crm.area.categories/search"
	_description = "Categories CRM Area"

class ViewModelFindCrmAreaCategories(ViewModelFindController):
	_name = "find:crm.area.categories"
	_view_name = "crm.area.categories/find"
	_description = "Categories CRM Area"

class ViewModelListCrmAreaCategories(ViewModelListController):
	_name = "list:crm.area.categories"
	_view_name = "crm.area.categories/list"
	_description = "Categories CRM Area"

class ViewModelFormModalCrmAreaCategories(ViewModelFormModalController):
	_name = "form.modal:crm.area.categories"
	_view_name = "crm.area.categories/form.modal"
	_description = "Categories CRM Area"

class ViewModelFormCrmAreaCategories(ViewModelFormController):
	_name = "form:crm.area.categories"
	_view_name = "crm.area.categories/form"
	_description = "Categories CRM Area"

class ViewModelTreeCrmAreaCategories(ViewModelTreeController):
	_name = "tree:crm.area.categories"
	_view_name = "crm.area.categories/tree"
	_description = "Categories CRM Area"
