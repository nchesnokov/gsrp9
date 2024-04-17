from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCrmContractCategories(ViewModelSearchController):
	_name = "search:crm.contract.categories"
	_view_name = "crm.contract.categories/search"
	_description = "Category Contract"

class ViewModelFindCrmContractCategories(ViewModelFindController):
	_name = "find:crm.contract.categories"
	_view_name = "crm.contract.categories/find"
	_description = "Category Contract"

class ViewModelListCrmContractCategories(ViewModelListController):
	_name = "list:crm.contract.categories"
	_view_name = "crm.contract.categories/list"
	_description = "Category Contract"

class ViewModelFormModalCrmContractCategories(ViewModelFormModalController):
	_name = "form.modal:crm.contract.categories"
	_view_name = "crm.contract.categories/form.modal"
	_description = "Category Contract"

class ViewModelFormCrmContractCategories(ViewModelFormController):
	_name = "form:crm.contract.categories"
	_view_name = "crm.contract.categories/form"
	_description = "Category Contract"

class ViewModelTreeCrmContractCategories(ViewModelTreeController):
	_name = "tree:crm.contract.categories"
	_view_name = "crm.contract.categories/tree"
	_description = "Category Contract"
