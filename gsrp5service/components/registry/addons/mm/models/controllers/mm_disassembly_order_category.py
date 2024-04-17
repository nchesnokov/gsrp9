from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmDisassemblyOrderCategory(ViewModelSearchController):
	_name = "search:mm.disassembly.order.category"
	_view_name = "mm.disassembly.order.category/search"
	_description = "Category Disassembly Order"

class ViewModelFindMmDisassemblyOrderCategory(ViewModelFindController):
	_name = "find:mm.disassembly.order.category"
	_view_name = "mm.disassembly.order.category/find"
	_description = "Category Disassembly Order"

class ViewModelListMmDisassemblyOrderCategory(ViewModelListController):
	_name = "list:mm.disassembly.order.category"
	_view_name = "mm.disassembly.order.category/list"
	_description = "Category Disassembly Order"

class ViewModelFormModalMmDisassemblyOrderCategory(ViewModelFormModalController):
	_name = "form.modal:mm.disassembly.order.category"
	_view_name = "mm.disassembly.order.category/form.modal"
	_description = "Category Disassembly Order"

class ViewModelFormMmDisassemblyOrderCategory(ViewModelFormController):
	_name = "form:mm.disassembly.order.category"
	_view_name = "mm.disassembly.order.category/form"
	_description = "Category Disassembly Order"

class ViewModelTreeMmDisassemblyOrderCategory(ViewModelTreeController):
	_name = "tree:mm.disassembly.order.category"
	_view_name = "mm.disassembly.order.category/tree"
	_description = "Category Disassembly Order"
