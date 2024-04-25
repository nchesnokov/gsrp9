from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmDisassemblyOrderTypes(ViewModelSearchController):
	_name = "search:mm.disassembly.order.types"
	_view_name = "mm.disassembly.order.types/search"
	_description = "Types Disassembly Order"

class ViewModelFindMmDisassemblyOrderTypes(ViewModelFindController):
	_name = "find:mm.disassembly.order.types"
	_view_name = "mm.disassembly.order.types/find"
	_description = "Types Disassembly Order"

class ViewModelListMmDisassemblyOrderTypes(ViewModelListController):
	_name = "list:mm.disassembly.order.types"
	_view_name = "mm.disassembly.order.types/list"
	_description = "Types Disassembly Order"

class ViewModelFormModalMmDisassemblyOrderTypes(ViewModelFormModalController):
	_name = "form.modal:mm.disassembly.order.types"
	_view_name = "mm.disassembly.order.types/form.modal"
	_description = "Types Disassembly Order"

class ViewModelFormMmDisassemblyOrderTypes(ViewModelFormController):
	_name = "form:mm.disassembly.order.types"
	_view_name = "mm.disassembly.order.types/form"
	_description = "Types Disassembly Order"
