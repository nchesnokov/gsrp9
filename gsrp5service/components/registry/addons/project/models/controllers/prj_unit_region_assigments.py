from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjUnitRegionAssigments(ViewModelSearchController):
	_name = "search:prj.unit.region.assigments"
	_view_name = "prj.unit.region.assigments/search"
	_description = "Project Unit Of Region Assigment"

class ViewModelFindPrjUnitRegionAssigments(ViewModelFindController):
	_name = "find:prj.unit.region.assigments"
	_view_name = "prj.unit.region.assigments/find"
	_description = "Project Unit Of Region Assigment"

class ViewModelListPrjUnitRegionAssigments(ViewModelListController):
	_name = "list:prj.unit.region.assigments"
	_view_name = "prj.unit.region.assigments/list"
	_description = "Project Unit Of Region Assigment"

class ViewModelFormModalPrjUnitRegionAssigments(ViewModelFormModalController):
	_name = "form.modal:prj.unit.region.assigments"
	_view_name = "prj.unit.region.assigments/form.modal"
	_description = "Project Unit Of Region Assigment"

class ViewModelFormPrjUnitRegionAssigments(ViewModelFormController):
	_name = "form:prj.unit.region.assigments"
	_view_name = "prj.unit.region.assigments/form"
	_description = "Project Unit Of Region Assigment"
