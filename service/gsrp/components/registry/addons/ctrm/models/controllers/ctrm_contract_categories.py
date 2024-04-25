from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCtrmContractCategories(ViewModelSearchController):
	_name = "search:ctrm.contract.categories"
	_view_name = "ctrm.contract.categories/search"
	_description = "Category CTRM Contract"

class ViewModelFindCtrmContractCategories(ViewModelFindController):
	_name = "find:ctrm.contract.categories"
	_view_name = "ctrm.contract.categories/find"
	_description = "Category CTRM Contract"

class ViewModelListCtrmContractCategories(ViewModelListController):
	_name = "list:ctrm.contract.categories"
	_view_name = "ctrm.contract.categories/list"
	_description = "Category CTRM Contract"

class ViewModelFormModalCtrmContractCategories(ViewModelFormModalController):
	_name = "form.modal:ctrm.contract.categories"
	_view_name = "ctrm.contract.categories/form.modal"
	_description = "Category CTRM Contract"

class ViewModelFormCtrmContractCategories(ViewModelFormController):
	_name = "form:ctrm.contract.categories"
	_view_name = "ctrm.contract.categories/form"
	_description = "Category CTRM Contract"

class ViewModelTreeCtrmContractCategories(ViewModelTreeController):
	_name = "tree:ctrm.contract.categories"
	_view_name = "ctrm.contract.categories/tree"
	_description = "Category CTRM Contract"
