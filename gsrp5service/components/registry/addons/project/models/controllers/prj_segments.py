from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjSegments(ViewModelSearchController):
	_name = "search:prj.segments"
	_view_name = "prj.segments/search"
	_description = "Project Segments"

class ViewModelFindPrjSegments(ViewModelFindController):
	_name = "find:prj.segments"
	_view_name = "prj.segments/find"
	_description = "Project Segments"

class ViewModelListPrjSegments(ViewModelListController):
	_name = "list:prj.segments"
	_view_name = "prj.segments/list"
	_description = "Project Segments"

class ViewModelFormModalPrjSegments(ViewModelFormModalController):
	_name = "form.modal:prj.segments"
	_view_name = "prj.segments/form.modal"
	_description = "Project Segments"

class ViewModelFormPrjSegments(ViewModelFormController):
	_name = "form:prj.segments"
	_view_name = "prj.segments/form"
	_description = "Project Segments"
