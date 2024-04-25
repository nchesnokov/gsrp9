from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmDivisionCategories(ViewModelSearchController):
	_name = "search:crm.division.categories"
	_view_name = "crm.division.categories/search"
	_description = "Categories CRM Division"

class ViewModelFindCrmDivisionCategories(ViewModelFindController):
	_name = "find:crm.division.categories"
	_view_name = "crm.division.categories/find"
	_description = "Categories CRM Division"

class ViewModelListCrmDivisionCategories(ViewModelListController):
	_name = "list:crm.division.categories"
	_view_name = "crm.division.categories/list"
	_description = "Categories CRM Division"

class ViewModelFormModalCrmDivisionCategories(ViewModelFormModalController):
	_name = "form.modal:crm.division.categories"
	_view_name = "crm.division.categories/form.modal"
	_description = "Categories CRM Division"

class ViewModelFormCrmDivisionCategories(ViewModelFormController):
	_name = "form:crm.division.categories"
	_view_name = "crm.division.categories/form"
	_description = "Categories CRM Division"

class ViewModelTreeCrmDivisionCategories(ViewModelTreeController):
	_name = "tree:crm.division.categories"
	_view_name = "crm.division.categories/tree"
	_description = "Categories CRM Division"
