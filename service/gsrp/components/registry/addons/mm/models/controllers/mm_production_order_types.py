from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmProductionOrderTypes(ViewModelSearchController):
	_name = "search:mm.production.order.types"
	_view_name = "mm.production.order.types/search"
	_description = "Types Production Order"

class ViewModelFindMmProductionOrderTypes(ViewModelFindController):
	_name = "find:mm.production.order.types"
	_view_name = "mm.production.order.types/find"
	_description = "Types Production Order"

class ViewModelListMmProductionOrderTypes(ViewModelListController):
	_name = "list:mm.production.order.types"
	_view_name = "mm.production.order.types/list"
	_description = "Types Production Order"

class ViewModelFormModalMmProductionOrderTypes(ViewModelFormModalController):
	_name = "form.modal:mm.production.order.types"
	_view_name = "mm.production.order.types/form.modal"
	_description = "Types Production Order"

class ViewModelFormMmProductionOrderTypes(ViewModelFormController):
	_name = "form:mm.production.order.types"
	_view_name = "mm.production.order.types/form"
	_description = "Types Production Order"
