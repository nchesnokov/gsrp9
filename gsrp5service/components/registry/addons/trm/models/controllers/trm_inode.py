from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchTrmInode(ViewModelSearchController):
	_name = "search:trm.inode"
	_view_name = "trm.inode/search"
	_description = "Node"

class ViewModelFindTrmInode(ViewModelFindController):
	_name = "find:trm.inode"
	_view_name = "trm.inode/find"
	_description = "Node"

class ViewModelListTrmInode(ViewModelListController):
	_name = "list:trm.inode"
	_view_name = "trm.inode/list"
	_description = "Node"

class ViewModelFormModalTrmInode(ViewModelFormModalController):
	_name = "form.modal:trm.inode"
	_view_name = "trm.inode/form.modal"
	_description = "Node"

class ViewModelFormTrmInode(ViewModelFormController):
	_name = "form:trm.inode"
	_view_name = "trm.inode/form"
	_description = "Node"
