from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchTmNodes(ViewModelSearchController):
	_name = "search:tm.nodes"
	_view_name = "tm.nodes/search"
	_description = "Nodes"

class ViewModelFindTmNodes(ViewModelFindController):
	_name = "find:tm.nodes"
	_view_name = "tm.nodes/find"
	_description = "Nodes"

class ViewModelListTmNodes(ViewModelListController):
	_name = "list:tm.nodes"
	_view_name = "tm.nodes/list"
	_description = "Nodes"

class ViewModelFormModalTmNodes(ViewModelFormModalController):
	_name = "form.modal:tm.nodes"
	_view_name = "tm.nodes/form.modal"
	_description = "Nodes"

class ViewModelFormTmNodes(ViewModelFormController):
	_name = "form:tm.nodes"
	_view_name = "tm.nodes/form"
	_description = "Nodes"

class ViewModelTreeTmNodes(ViewModelTreeController):
	_name = "tree:tm.nodes"
	_view_name = "tm.nodes/tree"
	_description = "Nodes"
