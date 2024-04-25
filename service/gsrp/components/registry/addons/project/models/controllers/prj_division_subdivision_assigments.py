from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchPrjDivisionSubdivisionAssigments(ViewModelSearchController):
	_name = "search:prj.division.subdivision.assigments"
	_view_name = "prj.division.subdivision.assigments/search"
	_description = "Project Division Of Subdivision Assigment"

class ViewModelFindPrjDivisionSubdivisionAssigments(ViewModelFindController):
	_name = "find:prj.division.subdivision.assigments"
	_view_name = "prj.division.subdivision.assigments/find"
	_description = "Project Division Of Subdivision Assigment"

class ViewModelListPrjDivisionSubdivisionAssigments(ViewModelListController):
	_name = "list:prj.division.subdivision.assigments"
	_view_name = "prj.division.subdivision.assigments/list"
	_description = "Project Division Of Subdivision Assigment"

class ViewModelFormModalPrjDivisionSubdivisionAssigments(ViewModelFormModalController):
	_name = "form.modal:prj.division.subdivision.assigments"
	_view_name = "prj.division.subdivision.assigments/form.modal"
	_description = "Project Division Of Subdivision Assigment"

class ViewModelFormPrjDivisionSubdivisionAssigments(ViewModelFormController):
	_name = "form:prj.division.subdivision.assigments"
	_view_name = "prj.division.subdivision.assigments/form"
	_description = "Project Division Of Subdivision Assigment"
