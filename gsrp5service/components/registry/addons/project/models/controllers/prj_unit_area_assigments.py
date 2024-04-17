from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjUnitAreaAssigments(ViewModelSearchController):
	_name = "search:prj.unit.area.assigments"
	_view_name = "prj.unit.area.assigments/search"
	_description = "Project Unit Of Area Assigment"

class ViewModelFindPrjUnitAreaAssigments(ViewModelFindController):
	_name = "find:prj.unit.area.assigments"
	_view_name = "prj.unit.area.assigments/find"
	_description = "Project Unit Of Area Assigment"

class ViewModelListPrjUnitAreaAssigments(ViewModelListController):
	_name = "list:prj.unit.area.assigments"
	_view_name = "prj.unit.area.assigments/list"
	_description = "Project Unit Of Area Assigment"

class ViewModelFormModalPrjUnitAreaAssigments(ViewModelFormModalController):
	_name = "form.modal:prj.unit.area.assigments"
	_view_name = "prj.unit.area.assigments/form.modal"
	_description = "Project Unit Of Area Assigment"

class ViewModelFormPrjUnitAreaAssigments(ViewModelFormController):
	_name = "form:prj.unit.area.assigments"
	_view_name = "prj.unit.area.assigments/form"
	_description = "Project Unit Of Area Assigment"
