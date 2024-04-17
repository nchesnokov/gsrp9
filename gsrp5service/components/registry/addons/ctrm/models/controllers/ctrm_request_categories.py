from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchCtrmRequestCategories(ViewModelSearchController):
	_name = "search:ctrm.request.categories"
	_view_name = "ctrm.request.categories/search"
	_description = "Category CTRM Request"

class ViewModelFindCtrmRequestCategories(ViewModelFindController):
	_name = "find:ctrm.request.categories"
	_view_name = "ctrm.request.categories/find"
	_description = "Category CTRM Request"

class ViewModelListCtrmRequestCategories(ViewModelListController):
	_name = "list:ctrm.request.categories"
	_view_name = "ctrm.request.categories/list"
	_description = "Category CTRM Request"

class ViewModelFormModalCtrmRequestCategories(ViewModelFormModalController):
	_name = "form.modal:ctrm.request.categories"
	_view_name = "ctrm.request.categories/form.modal"
	_description = "Category CTRM Request"

class ViewModelFormCtrmRequestCategories(ViewModelFormController):
	_name = "form:ctrm.request.categories"
	_view_name = "ctrm.request.categories/form"
	_description = "Category CTRM Request"

class ViewModelTreeCtrmRequestCategories(ViewModelTreeController):
	_name = "tree:ctrm.request.categories"
	_view_name = "ctrm.request.categories/tree"
	_description = "Category CTRM Request"
