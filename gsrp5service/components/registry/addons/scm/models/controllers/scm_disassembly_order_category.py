from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchScmDisassemblyOrderCategory(ViewModelSearchController):
	_name = "search:scm.disassembly.order.category"
	_view_name = "scm.disassembly.order.category/search"
	_description = "Category Disassembly Order"

class ViewModelFindScmDisassemblyOrderCategory(ViewModelFindController):
	_name = "find:scm.disassembly.order.category"
	_view_name = "scm.disassembly.order.category/find"
	_description = "Category Disassembly Order"

class ViewModelListScmDisassemblyOrderCategory(ViewModelListController):
	_name = "list:scm.disassembly.order.category"
	_view_name = "scm.disassembly.order.category/list"
	_description = "Category Disassembly Order"

class ViewModelFormModalScmDisassemblyOrderCategory(ViewModelFormModalController):
	_name = "form.modal:scm.disassembly.order.category"
	_view_name = "scm.disassembly.order.category/form.modal"
	_description = "Category Disassembly Order"

class ViewModelFormScmDisassemblyOrderCategory(ViewModelFormController):
	_name = "form:scm.disassembly.order.category"
	_view_name = "scm.disassembly.order.category/form"
	_description = "Category Disassembly Order"

class ViewModelTreeScmDisassemblyOrderCategory(ViewModelTreeController):
	_name = "tree:scm.disassembly.order.category"
	_view_name = "scm.disassembly.order.category/tree"
	_description = "Category Disassembly Order"
