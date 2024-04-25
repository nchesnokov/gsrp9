from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchEhsDisassemblyOrderCategory(ViewModelSearchController):
	_name = "search:ehs.disassembly.order.category"
	_view_name = "ehs.disassembly.order.category/search"
	_description = "Category Disassembly Order"

class ViewModelFindEhsDisassemblyOrderCategory(ViewModelFindController):
	_name = "find:ehs.disassembly.order.category"
	_view_name = "ehs.disassembly.order.category/find"
	_description = "Category Disassembly Order"

class ViewModelListEhsDisassemblyOrderCategory(ViewModelListController):
	_name = "list:ehs.disassembly.order.category"
	_view_name = "ehs.disassembly.order.category/list"
	_description = "Category Disassembly Order"

class ViewModelFormModalEhsDisassemblyOrderCategory(ViewModelFormModalController):
	_name = "form.modal:ehs.disassembly.order.category"
	_view_name = "ehs.disassembly.order.category/form.modal"
	_description = "Category Disassembly Order"

class ViewModelFormEhsDisassemblyOrderCategory(ViewModelFormController):
	_name = "form:ehs.disassembly.order.category"
	_view_name = "ehs.disassembly.order.category/form"
	_description = "Category Disassembly Order"

class ViewModelTreeEhsDisassemblyOrderCategory(ViewModelTreeController):
	_name = "tree:ehs.disassembly.order.category"
	_view_name = "ehs.disassembly.order.category/tree"
	_description = "Category Disassembly Order"
