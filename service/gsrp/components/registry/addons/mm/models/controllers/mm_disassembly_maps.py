from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmDisassemblyMaps(ViewModelSearchController):
	_name = "search:mm.disassembly.maps"
	_view_name = "mm.disassembly.maps/search"
	_description = "Disassembly map"

class ViewModelFindMmDisassemblyMaps(ViewModelFindController):
	_name = "find:mm.disassembly.maps"
	_view_name = "mm.disassembly.maps/find"
	_description = "Disassembly map"

class ViewModelListMmDisassemblyMaps(ViewModelListController):
	_name = "list:mm.disassembly.maps"
	_view_name = "mm.disassembly.maps/list"
	_description = "Disassembly map"

class ViewModelFormModalMmDisassemblyMaps(ViewModelFormModalController):
	_name = "form.modal:mm.disassembly.maps"
	_view_name = "mm.disassembly.maps/form.modal"
	_description = "Disassembly map"

class ViewModelFormMmDisassemblyMaps(ViewModelFormController):
	_name = "form:mm.disassembly.maps"
	_view_name = "mm.disassembly.maps/form"
	_description = "Disassembly map"
