from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchTmNodeItems(ViewModelSearchController):
	_name = "search:tm.node.items"
	_view_name = "tm.node.items/search"
	_description = "Node Items"

class ViewModelFindTmNodeItems(ViewModelFindController):
	_name = "find:tm.node.items"
	_view_name = "tm.node.items/find"
	_description = "Node Items"

class ViewModelListTmNodeItems(ViewModelListController):
	_name = "list:tm.node.items"
	_view_name = "tm.node.items/list"
	_description = "Node Items"

class ViewModelFormModalTmNodeItems(ViewModelFormModalController):
	_name = "form.modal:tm.node.items"
	_view_name = "tm.node.items/form.modal"
	_description = "Node Items"

class ViewModelFormTmNodeItems(ViewModelFormController):
	_name = "form:tm.node.items"
	_view_name = "tm.node.items/form"
	_description = "Node Items"

class ViewModelTreeTmNodeItems(ViewModelTreeController):
	_name = "tree:tm.node.items"
	_view_name = "tm.node.items/tree"
	_description = "Node Items"
