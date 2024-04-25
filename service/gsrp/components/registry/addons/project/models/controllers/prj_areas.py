from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjAreas(ViewModelSearchController):
	_name = "search:prj.areas"
	_view_name = "prj.areas/search"
	_description = "Project Areas"

class ViewModelFindPrjAreas(ViewModelFindController):
	_name = "find:prj.areas"
	_view_name = "prj.areas/find"
	_description = "Project Areas"

class ViewModelListPrjAreas(ViewModelListController):
	_name = "list:prj.areas"
	_view_name = "prj.areas/list"
	_description = "Project Areas"

class ViewModelFormModalPrjAreas(ViewModelFormModalController):
	_name = "form.modal:prj.areas"
	_view_name = "prj.areas/form.modal"
	_description = "Project Areas"

class ViewModelFormPrjAreas(ViewModelFormController):
	_name = "form:prj.areas"
	_view_name = "prj.areas/form"
	_description = "Project Areas"
