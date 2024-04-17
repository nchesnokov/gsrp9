from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjSubdivisions(ViewModelSearchController):
	_name = "search:prj.subdivisions"
	_view_name = "prj.subdivisions/search"
	_description = "Project Subdivisions"

class ViewModelFindPrjSubdivisions(ViewModelFindController):
	_name = "find:prj.subdivisions"
	_view_name = "prj.subdivisions/find"
	_description = "Project Subdivisions"

class ViewModelListPrjSubdivisions(ViewModelListController):
	_name = "list:prj.subdivisions"
	_view_name = "prj.subdivisions/list"
	_description = "Project Subdivisions"

class ViewModelFormModalPrjSubdivisions(ViewModelFormModalController):
	_name = "form.modal:prj.subdivisions"
	_view_name = "prj.subdivisions/form.modal"
	_description = "Project Subdivisions"

class ViewModelFormPrjSubdivisions(ViewModelFormController):
	_name = "form:prj.subdivisions"
	_view_name = "prj.subdivisions/form"
	_description = "Project Subdivisions"
