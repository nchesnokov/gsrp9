from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmRegions(ViewModelSearchController):
	_name = "search:srm.regions"
	_view_name = "srm.regions/search"
	_description = "SRM Regions"

class ViewModelFindSrmRegions(ViewModelFindController):
	_name = "find:srm.regions"
	_view_name = "srm.regions/find"
	_description = "SRM Regions"

class ViewModelListSrmRegions(ViewModelListController):
	_name = "list:srm.regions"
	_view_name = "srm.regions/list"
	_description = "SRM Regions"

class ViewModelFormModalSrmRegions(ViewModelFormModalController):
	_name = "form.modal:srm.regions"
	_view_name = "srm.regions/form.modal"
	_description = "SRM Regions"

class ViewModelFormSrmRegions(ViewModelFormController):
	_name = "form:srm.regions"
	_view_name = "srm.regions/form"
	_description = "SRM Regions"
