from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchBcGroupModules(ViewModelSearchController):
	_name = "search:bc.group.modules"
	_view_name = "bc.group.modules/search"
	_description = "Module Groups"

class ViewModelFindBcGroupModules(ViewModelFindController):
	_name = "find:bc.group.modules"
	_view_name = "bc.group.modules/find"
	_description = "Module Groups"

class ViewModelListBcGroupModules(ViewModelListController):
	_name = "list:bc.group.modules"
	_view_name = "bc.group.modules/list"
	_description = "Module Groups"

class ViewModelFormModalBcGroupModules(ViewModelFormModalController):
	_name = "form.modal:bc.group.modules"
	_view_name = "bc.group.modules/form.modal"
	_description = "Module Groups"

class ViewModelFormBcGroupModules(ViewModelFormController):
	_name = "form:bc.group.modules"
	_view_name = "bc.group.modules/form"
	_description = "Module Groups"

class ViewModelTreeBcGroupModules(ViewModelTreeController):
	_name = "tree:bc.group.modules"
	_view_name = "bc.group.modules/tree"
	_description = "Module Groups"
