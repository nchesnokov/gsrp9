from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmSubdivisionCategories(ViewModelSearchController):
	_name = "search:crm.subdivision.categories"
	_view_name = "crm.subdivision.categories/search"
	_description = "Categories CRM Subdivision"

class ViewModelFindCrmSubdivisionCategories(ViewModelFindController):
	_name = "find:crm.subdivision.categories"
	_view_name = "crm.subdivision.categories/find"
	_description = "Categories CRM Subdivision"

class ViewModelListCrmSubdivisionCategories(ViewModelListController):
	_name = "list:crm.subdivision.categories"
	_view_name = "crm.subdivision.categories/list"
	_description = "Categories CRM Subdivision"

class ViewModelFormModalCrmSubdivisionCategories(ViewModelFormModalController):
	_name = "form.modal:crm.subdivision.categories"
	_view_name = "crm.subdivision.categories/form.modal"
	_description = "Categories CRM Subdivision"

class ViewModelFormCrmSubdivisionCategories(ViewModelFormController):
	_name = "form:crm.subdivision.categories"
	_view_name = "crm.subdivision.categories/form"
	_description = "Categories CRM Subdivision"

class ViewModelTreeCrmSubdivisionCategories(ViewModelTreeController):
	_name = "tree:crm.subdivision.categories"
	_view_name = "crm.subdivision.categories/tree"
	_description = "Categories CRM Subdivision"
