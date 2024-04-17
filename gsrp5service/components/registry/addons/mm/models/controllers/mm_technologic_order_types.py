from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmTechnologicOrderTypes(ViewModelSearchController):
	_name = "search:mm.technologic.order.types"
	_view_name = "mm.technologic.order.types/search"
	_description = "Types Technologic Order"

class ViewModelFindMmTechnologicOrderTypes(ViewModelFindController):
	_name = "find:mm.technologic.order.types"
	_view_name = "mm.technologic.order.types/find"
	_description = "Types Technologic Order"

class ViewModelListMmTechnologicOrderTypes(ViewModelListController):
	_name = "list:mm.technologic.order.types"
	_view_name = "mm.technologic.order.types/list"
	_description = "Types Technologic Order"

class ViewModelFormModalMmTechnologicOrderTypes(ViewModelFormModalController):
	_name = "form.modal:mm.technologic.order.types"
	_view_name = "mm.technologic.order.types/form.modal"
	_description = "Types Technologic Order"

class ViewModelFormMmTechnologicOrderTypes(ViewModelFormController):
	_name = "form:mm.technologic.order.types"
	_view_name = "mm.technologic.order.types/form"
	_description = "Types Technologic Order"
