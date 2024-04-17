from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchMmTechnologicMaps(ViewModelSearchController):
	_name = "search:mm.technologic.maps"
	_view_name = "mm.technologic.maps/search"
	_description = "Technologic Map"

class ViewModelFindMmTechnologicMaps(ViewModelFindController):
	_name = "find:mm.technologic.maps"
	_view_name = "mm.technologic.maps/find"
	_description = "Technologic Map"

class ViewModelListMmTechnologicMaps(ViewModelListController):
	_name = "list:mm.technologic.maps"
	_view_name = "mm.technologic.maps/list"
	_description = "Technologic Map"

class ViewModelFormModalMmTechnologicMaps(ViewModelFormModalController):
	_name = "form.modal:mm.technologic.maps"
	_view_name = "mm.technologic.maps/form.modal"
	_description = "Technologic Map"

class ViewModelFormMmTechnologicMaps(ViewModelFormController):
	_name = "form:mm.technologic.maps"
	_view_name = "mm.technologic.maps/form"
	_description = "Technologic Map"
