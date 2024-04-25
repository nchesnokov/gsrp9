from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelTreeController

class ViewModelSearchMmDisassemblyMapCategory(ViewModelSearchController):
	_name = "search:mm.disassembly.map.category"
	_view_name = "mm.disassembly.map.category/search"
	_description = "Category Disassembly Map"

class ViewModelFindMmDisassemblyMapCategory(ViewModelFindController):
	_name = "find:mm.disassembly.map.category"
	_view_name = "mm.disassembly.map.category/find"
	_description = "Category Disassembly Map"

class ViewModelListMmDisassemblyMapCategory(ViewModelListController):
	_name = "list:mm.disassembly.map.category"
	_view_name = "mm.disassembly.map.category/list"
	_description = "Category Disassembly Map"

class ViewModelFormModalMmDisassemblyMapCategory(ViewModelFormModalController):
	_name = "form.modal:mm.disassembly.map.category"
	_view_name = "mm.disassembly.map.category/form.modal"
	_description = "Category Disassembly Map"

class ViewModelFormMmDisassemblyMapCategory(ViewModelFormController):
	_name = "form:mm.disassembly.map.category"
	_view_name = "mm.disassembly.map.category/form"
	_description = "Category Disassembly Map"

class ViewModelTreeMmDisassemblyMapCategory(ViewModelTreeController):
	_name = "tree:mm.disassembly.map.category"
	_view_name = "mm.disassembly.map.category/tree"
	_description = "Category Disassembly Map"
