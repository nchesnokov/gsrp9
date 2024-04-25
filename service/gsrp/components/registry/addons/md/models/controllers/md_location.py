from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController
from gsrp5service.obj.controller.controller import ViewModelGeoController

class ViewModelSearchMdLocation(ViewModelSearchController):
	_name = "search:md.location"
	_view_name = "md.location/search"
	_description = "Location"

class ViewModelFindMdLocation(ViewModelFindController):
	_name = "find:md.location"
	_view_name = "md.location/find"
	_description = "Location"

class ViewModelListMdLocation(ViewModelListController):
	_name = "list:md.location"
	_view_name = "md.location/list"
	_description = "Location"

class ViewModelFormModalMdLocation(ViewModelFormModalController):
	_name = "form.modal:md.location"
	_view_name = "md.location/form.modal"
	_description = "Location"

class ViewModelFormMdLocation(ViewModelFormController):
	_name = "form:md.location"
	_view_name = "md.location/form"
	_description = "Location"

class ViewModelGeoMdLocation(ViewModelGeoController):
	_name = "geo:md.location"
	_view_name = "md.location/geo"
	_description = "Location"
