from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmProductionMaps(ViewModelSearchController):
	_name = "search:mm.production.maps"
	_view_name = "mm.production.maps/search"
	_description = "Production Map"

class ViewModelFindMmProductionMaps(ViewModelFindController):
	_name = "find:mm.production.maps"
	_view_name = "mm.production.maps/find"
	_description = "Production Map"

class ViewModelListMmProductionMaps(ViewModelListController):
	_name = "list:mm.production.maps"
	_view_name = "mm.production.maps/list"
	_description = "Production Map"

class ViewModelFormModalMmProductionMaps(ViewModelFormModalController):
	_name = "form.modal:mm.production.maps"
	_view_name = "mm.production.maps/form.modal"
	_description = "Production Map"

class ViewModelFormMmProductionMaps(ViewModelFormController):
	_name = "form:mm.production.maps"
	_view_name = "mm.production.maps/form"
	_description = "Production Map"
