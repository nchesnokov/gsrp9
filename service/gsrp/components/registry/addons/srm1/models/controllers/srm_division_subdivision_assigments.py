from gsrp5service.obj.controller.controller import ViewModelSearchController
from gsrp5service.obj.controller.controller import ViewModelFindController
from gsrp5service.obj.controller.controller import ViewModelListController
from gsrp5service.obj.controller.controller import ViewModelFormModalController
from gsrp5service.obj.controller.controller import ViewModelFormController

class ViewModelSearchSrmDivisionSubdivisionAssigments(ViewModelSearchController):
	_name = "search:srm.division.subdivision.assigments"
	_view_name = "srm.division.subdivision.assigments/search"
	_description = "SRM Division Of Subdivision Assigment"

class ViewModelFindSrmDivisionSubdivisionAssigments(ViewModelFindController):
	_name = "find:srm.division.subdivision.assigments"
	_view_name = "srm.division.subdivision.assigments/find"
	_description = "SRM Division Of Subdivision Assigment"

class ViewModelListSrmDivisionSubdivisionAssigments(ViewModelListController):
	_name = "list:srm.division.subdivision.assigments"
	_view_name = "srm.division.subdivision.assigments/list"
	_description = "SRM Division Of Subdivision Assigment"

class ViewModelFormModalSrmDivisionSubdivisionAssigments(ViewModelFormModalController):
	_name = "form.modal:srm.division.subdivision.assigments"
	_view_name = "srm.division.subdivision.assigments/form.modal"
	_description = "SRM Division Of Subdivision Assigment"

class ViewModelFormSrmDivisionSubdivisionAssigments(ViewModelFormController):
	_name = "form:srm.division.subdivision.assigments"
	_view_name = "srm.division.subdivision.assigments/form"
	_description = "SRM Division Of Subdivision Assigment"
