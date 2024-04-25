from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjRegions(ViewModelSearchController):
	_name = "search:prj.regions"
	_view_name = "prj.regions/search"
	_description = "Project Regions"

class ViewModelFindPrjRegions(ViewModelFindController):
	_name = "find:prj.regions"
	_view_name = "prj.regions/find"
	_description = "Project Regions"

class ViewModelListPrjRegions(ViewModelListController):
	_name = "list:prj.regions"
	_view_name = "prj.regions/list"
	_description = "Project Regions"

class ViewModelFormModalPrjRegions(ViewModelFormModalController):
	_name = "form.modal:prj.regions"
	_view_name = "prj.regions/form.modal"
	_description = "Project Regions"

class ViewModelFormPrjRegions(ViewModelFormController):
	_name = "form:prj.regions"
	_view_name = "prj.regions/form"
	_description = "Project Regions"
