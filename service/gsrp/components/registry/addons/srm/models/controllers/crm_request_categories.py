from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmRequestCategories(ViewModelSearchController):
	_name = "search:crm.request.categories"
	_view_name = "crm.request.categories/search"
	_description = "Category CRM Request"

class ViewModelFindCrmRequestCategories(ViewModelFindController):
	_name = "find:crm.request.categories"
	_view_name = "crm.request.categories/find"
	_description = "Category CRM Request"

class ViewModelListCrmRequestCategories(ViewModelListController):
	_name = "list:crm.request.categories"
	_view_name = "crm.request.categories/list"
	_description = "Category CRM Request"

class ViewModelFormModalCrmRequestCategories(ViewModelFormModalController):
	_name = "form.modal:crm.request.categories"
	_view_name = "crm.request.categories/form.modal"
	_description = "Category CRM Request"

class ViewModelFormCrmRequestCategories(ViewModelFormController):
	_name = "form:crm.request.categories"
	_view_name = "crm.request.categories/form"
	_description = "Category CRM Request"

class ViewModelTreeCrmRequestCategories(ViewModelTreeController):
	_name = "tree:crm.request.categories"
	_view_name = "crm.request.categories/tree"
	_description = "Category CRM Request"
