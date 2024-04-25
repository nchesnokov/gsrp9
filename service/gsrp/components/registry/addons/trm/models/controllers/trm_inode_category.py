from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchTrmInodeCategory(ViewModelSearchController):
	_name = "search:trm.inode.category"
	_view_name = "trm.inode.category/search"
	_description = "Node Category"

class ViewModelFindTrmInodeCategory(ViewModelFindController):
	_name = "find:trm.inode.category"
	_view_name = "trm.inode.category/find"
	_description = "Node Category"

class ViewModelListTrmInodeCategory(ViewModelListController):
	_name = "list:trm.inode.category"
	_view_name = "trm.inode.category/list"
	_description = "Node Category"

class ViewModelFormModalTrmInodeCategory(ViewModelFormModalController):
	_name = "form.modal:trm.inode.category"
	_view_name = "trm.inode.category/form.modal"
	_description = "Node Category"

class ViewModelFormTrmInodeCategory(ViewModelFormController):
	_name = "form:trm.inode.category"
	_view_name = "trm.inode.category/form"
	_description = "Node Category"

class ViewModelTreeTrmInodeCategory(ViewModelTreeController):
	_name = "tree:trm.inode.category"
	_view_name = "trm.inode.category/tree"
	_description = "Node Category"
