from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchTmCategoryNode(ViewModelSearchController):
	_name = "search:tm.category.node"
	_view_name = "tm.category.node/search"
	_description = "Category Node"

class ViewModelFindTmCategoryNode(ViewModelFindController):
	_name = "find:tm.category.node"
	_view_name = "tm.category.node/find"
	_description = "Category Node"

class ViewModelListTmCategoryNode(ViewModelListController):
	_name = "list:tm.category.node"
	_view_name = "tm.category.node/list"
	_description = "Category Node"

class ViewModelFormModalTmCategoryNode(ViewModelFormModalController):
	_name = "form.modal:tm.category.node"
	_view_name = "tm.category.node/form.modal"
	_description = "Category Node"

class ViewModelFormTmCategoryNode(ViewModelFormController):
	_name = "form:tm.category.node"
	_view_name = "tm.category.node/form"
	_description = "Category Node"

class ViewModelTreeTmCategoryNode(ViewModelTreeController):
	_name = "tree:tm.category.node"
	_view_name = "tm.category.node/tree"
	_description = "Category Node"
