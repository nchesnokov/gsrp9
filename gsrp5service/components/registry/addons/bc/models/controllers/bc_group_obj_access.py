from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchBcGroupObjAccess(ViewModelSearchController):
	_name = "search:bc.group.obj.access"
	_view_name = "bc.group.obj.access/search"
	_description = "Group Object Access"

class ViewModelFindBcGroupObjAccess(ViewModelFindController):
	_name = "find:bc.group.obj.access"
	_view_name = "bc.group.obj.access/find"
	_description = "Group Object Access"

class ViewModelListBcGroupObjAccess(ViewModelListController):
	_name = "list:bc.group.obj.access"
	_view_name = "bc.group.obj.access/list"
	_description = "Group Object Access"

class ViewModelFormModalBcGroupObjAccess(ViewModelFormModalController):
	_name = "form.modal:bc.group.obj.access"
	_view_name = "bc.group.obj.access/form.modal"
	_description = "Group Object Access"

class ViewModelFormBcGroupObjAccess(ViewModelFormController):
	_name = "form:bc.group.obj.access"
	_view_name = "bc.group.obj.access/form"
	_description = "Group Object Access"

class ViewModelTreeBcGroupObjAccess(ViewModelTreeController):
	_name = "tree:bc.group.obj.access"
	_view_name = "bc.group.obj.access/tree"
	_description = "Group Object Access"
