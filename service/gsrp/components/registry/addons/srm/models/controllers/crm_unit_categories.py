from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmUnitCategories(ViewModelSearchController):
	_name = "search:crm.unit.categories"
	_view_name = "crm.unit.categories/search"
	_description = "Categories CRM Unit"

class ViewModelFindCrmUnitCategories(ViewModelFindController):
	_name = "find:crm.unit.categories"
	_view_name = "crm.unit.categories/find"
	_description = "Categories CRM Unit"

class ViewModelListCrmUnitCategories(ViewModelListController):
	_name = "list:crm.unit.categories"
	_view_name = "crm.unit.categories/list"
	_description = "Categories CRM Unit"

class ViewModelFormModalCrmUnitCategories(ViewModelFormModalController):
	_name = "form.modal:crm.unit.categories"
	_view_name = "crm.unit.categories/form.modal"
	_description = "Categories CRM Unit"

class ViewModelFormCrmUnitCategories(ViewModelFormController):
	_name = "form:crm.unit.categories"
	_view_name = "crm.unit.categories/form"
	_description = "Categories CRM Unit"

class ViewModelTreeCrmUnitCategories(ViewModelTreeController):
	_name = "tree:crm.unit.categories"
	_view_name = "crm.unit.categories/tree"
	_description = "Categories CRM Unit"
